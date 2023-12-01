import os
import time
from colorama import Fore, Style

from selenium_driver import SeleniumDriver


class HelloWork:

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.driver = SeleniumDriver(headless=False)
        return

    # ---------------- LOGIN -------------------- #

    def login(self) -> bool:
        self.driver.get('https://www.hellowork.com/fr-fr/candidat/connexion-inscription.html#connexion')
        time.sleep(2)
        self.driver.click('#hw-cc-notice-accept-btn')
        self.driver.write('input[type=email][name=email]', self.config['user']['email'])
        self.driver.write('input[type=email][name=email2]', self.config['user']['email'])
        self.driver.write('input[type=password][name=password]', self.config['user']['password'])
        self.driver.write('input[type=password][name=password2]', self.config['user']['password'])
        self.driver.click('form > button[data-simple-progress]')
        time.sleep(4)

        if 'candidat/connexion' not in self.driver.current_url():
            print(Fore.GREEN + 'logged in !')
            return True
        else:
            return False

    # ---------------- APPLICATION -------------------- #

    def application(self):
        self.driver.click('[data-cy="applyButton"]')
        time.sleep(1)

        # for handle in self.driver.window_handles():
        #     self.driver.switch_to_window(handle)

        print(self.driver.current_url())

        if '/bounce/similar' in self.driver.current_url() or '/offres/postulerexterneform' in self.driver.current_url() or self.driver.click('#postuler turbo-frame [data-cy="applyButton"]'):
            print('external application')
            while '/bounce/similar' in self.driver.current_url() or '/offres/postulerexterneform' in self.driver.current_url():
                for handle in self.driver.window_handles():
                    self.driver.switch_to_window(handle)
                print(self.driver.current_url())
                time.sleep(2)

            time.sleep(2)
            
            if 'taleez.com' in self.driver.current_url():

                labels = self.driver.find_elements('div.field > label.required, div.field.question > label')
                questions = self.driver.find_elements('div.field > tz-input input, tz-input-phone > input, tz-drag-file input, mat-radio-group > *:nth-child(1) input[type="radio"]')

                self.driver.write('tz-input-phone > input', self.config['setting']['presets']['phone'])

                for i in range(len(labels)):

                    try:
                        label = labels[i].get_property('innerText').lower()
                        # print(label)
                        question = questions[i]
                    except:
                        break

                    if question.get_property('type') == 'file':
                        question.send_keys(self.config['user']['cv'])

                    elif question.get_property('type') == 'text' or question.get_property('type') == 'email':

                        if question.get_property('value') != "":
                            continue

                        for preset in self.config['setting']['presets']:
                            if preset in label:
                                question.send_keys(self.config['setting']['presets'][preset])
                                # self.driver.write('', self.config['setting']['presets'][preset])
                                break

                    elif question.get_property('type') == 'radio':
                        question.click()
                
                self.driver.click('[formcontrolname="cgu"] input')
                time.sleep(1)
                self.driver.click('button[type="submit"]')
                time.sleep(3)

            # elif 'recrute.carrefour.com' in self.driver.current_url():
            #     time.sleep(999)

            # elif 'recrutement-reseau.renault.fr' in self.driver.current_url():
            #     pass

            # elif 'safran-group.com/fr/offres' in self.driver.current_url():
            #     pass

            else:
                print(Fore.RED + 'Nothing: ' + self.driver.current_url())

            time.sleep(1)
            self.driver.close()
            time.sleep(1)
            for handle in self.driver.window_handles():
                self.driver.switch_to_window(handle)

        else:
            print('internal application')
            
            self.driver.click('#btn-submit, [data-cy="submitButton"], [data-cy="saContinueButton"]')
            self.driver.click('#btn-submit, [data-cy="submitButton"], [data-cy="saContinueButton"]')

            # self.driver.click('[data-cy="saContinueButton"]')
            # self.driver.click('[data-cy="saContinueButton"]')
            time.sleep(3)

            if self.driver.is_attached('[data-cy="saNextStep"] > *'):
                
                labels = self.driver.find_elements('[data-smart-apply-target="nextStep"] label')
                questions = self.driver.find_elements('[data-smart-apply-target="nextStep"] input, [data-smart-apply-target="nextStep"] select')

                for i in range(len(labels)):
                    question = questions[i]
                    label = labels[i].get_property('innerText').strip()
                    print(label)

                    html_tag = question.get_property('localName')
                    print(html_tag)
                    ok = False

                    if html_tag == 'input':
                        question_type = question.get_property('type')
                        print(question_type)
                        
                        if question_type == 'text' or question_type == 'email':
                            for preset in self.config['setting']['presets']:
                                if preset in label:
                                    print(self.config['setting']['presets'][preset])
                                    question.send_keys(self.config['setting']['presets'][preset])
                                    ok = True
                                    break
                            if not ok:
                                question.send_keys('Oui')
                        continue

                    if html_tag == 'select':
                        for preset in self.config['setting']['presets']:
                            if preset in label:
                                for option in self.driver.find_elements('[data-smart-apply-target="nextStep"] select option'):
                                    if self.config['setting']['presets'][preset] in option.get_property('value'):
                                        option.click()
                                        ok = True
                                        break
                                if ok:
                                    break
                        if not ok:
                            self.driver.click(f'[data-smart-apply-target="nextStep"] select option:nth-child({i + 1})')
                        continue

            self.driver.click('#btn-submit, [data-cy="submitButton"]')
            self.driver.click('#btn-submit, [data-cy="submitButton"]')

            print(Fore.GREEN + '+1 application')


    def application_loop(self):
        if not self.login():
            return

        for listing_url in self.config['urls']:

            self.driver.get(listing_url)
            time.sleep(1)
            
            while self.driver.is_attached('#pagin li.s + li'):

                companie_name = self.driver.find_elements('[data-cy="companyName"]')
                jobs = self.driver.find_elements('.offer--maininfo a[data-ga]')
                i_job = -1

                print(f'{len(jobs)} jobs founded')
                for job in jobs:
                    i_job = i_job + 1
                    
                    # Checking if job_title is not excluded
                    ok = True
                    job_title = str(job.get_property('innerText')).lower()
                    print(job_title)
                    for ek in self.config['setting']['excluded_keywords']:
                        if ek in job_title:
                            ok = False
                    if not ok:
                        print(Fore.RED + 'excluded_keywords in job_title')
                        print(Style.RESET_ALL)
                        continue

                    # Checking if job_company is not excluded
                    ok = True
                    try:
                        job_company = companie_name[i_job]
                        job_company = job_company.get_property('innerText').lower()
                        print(job_company)
                        for ek in self.config['setting']['excluded_companies']:
                            if ek in job_company:
                                ok = False
                        if not ok:
                            print(Fore.RED + 'excluded_company in job_company')
                            print(Style.RESET_ALL)
                            continue
                    except:
                        print(Fore.RED + 'impossible to get company by listing sidebar')
                        print(Style.RESET_ALL)

                    job_url = job.get_property('href')
                    print(job_url)
                    self.driver.execute_script(f'window.open("{job_url}")')

                    for handle in self.driver.window_handles():
                        self.driver.switch_to_window(handle)
                    time.sleep(1)

                    self.application()
                    # time.sleep(4)

                    self.driver.close()
                    time.sleep(1)

                    self.driver.switch_to_window(self.driver.window_handles()[0])

                self.driver.click('#pagin li.s + li')

                time.sleep(2)

