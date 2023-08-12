from typing import Any, Dict, List, Union
import random
import socket 

hostname = socket.gethostname()
ip_adress = socket.gethostbyname(hostname)

password: str = "peneduro22"
colombia_cities = ["Bogotá", "Medellín", "Cartagena", "Cali", "Barranquilla"]


def get_dict(email: str, phone_number: str) -> Dict[str, List[Union[Any, Dict[str, Any]]]]:
    """
    This function returns a dictionaire with all the needed data to fill every form for 
    each website.
      ['key'][0] = url
      ['key'][1] = form
    """
    return {
        "brazino777": ["https://brazino777.com/api/register_new", {
            "bonus": "one_hundred_percent_on_first_deposit",
            "email": email,
            "login": email.split('@')[0],
            "password": password,
            "currency": "MXN"
        }],
        "graff-city": ["https://www.graff-city.com/register", {
            "form_identifier": "register",
            "csrf_token": "l2ATYO8I0Dx1ffm",
            "referer":" ",
            "enquiry_id":"591f69681213ee977039d46666f98fb9",
            "company_name":"Nigger Inc",
            "title":"Mr",
            "full_name":"Johnny Doe",
            "email_address": email,
            "your_password": password,
            "your_password_retype": password,
            "address1":"McKay Avenue 666",
            "address2":"",
            "town":"New York",
            "county":"",
            "country":"43",
            "postcode":"777666",
            "postcode_required":"",
            "telephone":"+150360790",
            "vat_number_country":"AZ",
            "eori_number":"",
            "newsletter_signup":"Y",
            "accept_terms":"Y",
            "register": ""
        }], 
       
        "krispymods": ["https://krispymods.com/my-account/", {
            "email": email,
            "password": password,
            "woocommerce-register-nonce": "989ba1dbc2",
            "_wp_http_referer": "/my-account/",
            "register": "Register"
        }],
        
        "snoopdoog": ["https://snoopdogg.com/wp-admin/admin-ajax.php", {
            'post_id': 176,
            'form_id': "53c9668",
            "referer_title'": "Home - Snoop Dogg",
            "queried_id'": 1781,
            "form_fields[email]": email,
            "action": "elementor_pro_forms_send_form",
            "referrer": "https://snoopdogg.com/"
        }],

        "larepublica": ["https://promociones.larepublica.pe/api/newsletter/save", {
            "category": "ultimas-noticias",
            "celular": "987654321",
            "departamento": "Arequipa",
            "dni": "",
            "edad": "26",
            "email": email,
            "firstname": "Emanuel",
            "gender": "hombre",
            "lastname": "Anthony",
            "medio": "larepublica",
            "nivel_educativo": "Técnica"
            }],

        "eluniversal": ["https://newsletter.eluniversal.com.mx/v1/newsletter/register-new-user", {
            "email": email,
            "nws": "nwsl31"
        }],

        "peruquiosco": ["https://id.tinypass.com/id/api/v1/identity/register/token", {
            "first_name": "Elver",
            "last_name": "Gonmez",
            "email": email,
            "password": password,
            "consents": [
                {
                "consent_pub_id": "CBCDSLTL3ROMW",
                "display_text": "Al crear la cuenta acepto los <a href=\"https://e.peruquiosco.pe/site/file/terminos_condiciones_pq.pdf?v1616353629\" target='_blank'>Términos y Condiciones</a> y <a href=\"https://e.peruquiosco.pe/site/file/politica_cookies.pdf?v1616353629\" target='_blank'>Política de Privacidad</a>",
                "field_name": "termsconditions",
                "field_id": "termsconditions",
                "sort_order": 0,
                "checked": True,
                "required": False
                },
                {
                "consent_pub_id": "CBCCL8BBZH144",
                "display_text": "Al registrarme autorizo el uso de mis datos para <a href=\"https://web.peruquiosco.pe/?page=tratamiento-datos\" target='_blank'>fines adicionales.</a>",
                "field_name": "datatreatment",
                "field_id": "datatreatment",
                "sort_order": 1,
                "checked": True,
                "required": False
                }
            ],
            "customFieldValues": [],
            "remember": True,
            "origin_url": "https://web.peruquiosco.pe/"
        }],

        "wattpad": ["https://www.wattpad.com/signup?nextUrl=/home", {
            "signup-from": "new_landing_signup",
            "form-type": "",
            "username": "jhonnnydoe",
            "email": email,
            "new_password": password,
            "confirm_password": password,
            "month": "09",
            "day": "17",
            "year": "1996"
        }],
        "quora": ["https://es.quora.com/graphql/gql_POST?q=SignupEmailBasicInfoModal_sendSignupEmailConfirmationEmail_Mutation", {
              "queryName": "SignupEmailBasicInfoModal_sendSignupEmailConfirmationEmail_Mutation",
            "variables": {
                "email": email
            },
            "extensions": {
                "hash": "5d6b42b7f164aeb88e0861471a72144093610a04c507617fa510d2b68c2e9dda"
            }       
        }],
        "nacc-th": ["https://itas.nacc.go.th/account/register", {
            "Email": email,
            "Password": "ksdfjdjfifjdf",
            "FirstName": "El",
            "LastName": "Papu",
            "PhoneNo": f"{random.randint(1000000, 10000000) if not phone_number else phone_number}",
            "UserSrcCatId": "4",
            "OrgName": "OSTdio",
            "__RequestVerificationToken": "CfDJ8Dty1nqi6PpChJszX2gO5wnkI7DTsgMmKWVEovhA23CVeVMOjNzqvbvHtERMIYKadTEkqGJZoI4fzb85x-s2homRsLukc91OEkKgT-9XzvxZeEskCBxb2kxIgGOkQw0aLpAkunJ9KUmV8hcjD7XxZaw",
            "6499BBDB": "8B8D05B1D5402C2DD69231F8F9FE66CA"
        }],
        "mailup": ["https://blog.mailup.es/sender/", {
            "CampaignID__c": "7012o000001bxxAAAQ",
            "OwnerId": "0052o000009FR3pAAG",
            "RecordTypeId": "Lead_Freddi",
            "Status": "Unqualified",
            "Team_Commerciale__c": "1+-+Italia",
            "Nazione__c": "IT",
            "Campaign_Member_Status__c": "Submit",
            "Informativa_Privacy__c": "true",
            "FromWebsite__c":"",
            "Aggiornamento_Punteggio__c": "",
            "Aggiornamento_Punteggio_Assegnazione__c": "",
            "form_type": "newsletter-optin-aside",
            "now": "Sat,+22+Jul+2023+23:53:40++0000",
            "part_maps": "",
            "token":	"71663616",
            "language":	"ES",
            "referer":	"https://blog.mailup.es/2021/08/boletines-marketing-digital/join-us-register-newsletter-concept/",
            "uri":	"/2021/08/boletines-marketing-digital/join-us-register-newsletter-concept/",
            "page_title":	"Join+Us+Register+Newsletter+Concept",
            "ip	": ip_adress,
            "host":	"blog.mailup.es",
            "http_host":	"blog.mailup.es",
            "user_agent":	"Amazon+CloudFront",
            "remote_address":	"",
            "google_recaptha":	"",
            "IPAddress__c":	"",
            "Client__c":	"Amazon+CloudFront",
            "Referer__c":	"https://blog.mailup.es/2021/08/boletines-marketing-digital/join-us-register-newsletter-concept/",
            "utm_source":	"",
            "utm_source__c":	"",
            "utm_medium":	"",
            "utm_medium__c":	"",
            "utm_campaign":	"",
            "utm_campaign__c":	"",
            "utm_term":	"",
            "utm_term__c": "",
            "utm_content": "",
            "utm_content__c": "",
            "FirstName": "Juan",
            "LastName": "Perez",
            "Company": "OSTdio",
            "Email": email,
            "Consenso_Lista51__c": "1"
        }],
        
        'futurelearn': ["https://www.futurelearn.com/register", {
            'authenticity_token': 'qym5UqrVK5cGvaILbLZcfgsVxn9Q3KqRLMEZlq9gffgMhhArBAKj8maOyTzSn0Idq3dSXCQgI9luEIt79ek3VQ',
            'utf8': '✓',
            'title': '',
            'user[first_name]': 'Elver Gonmez',
            'user[last_name]': 'Torba',
            'user[email]': email,
            'user[password]': password,
            'user[registration_email_preferences][]': 'announcement'
        }],

        "danteshoes": ['https://www.danteshoes.com/en/newsletter', {
            '_token': 'wvPqC0vSwbAEuwPmP014hpDh1xnLUNeabiPBO1mA',
            'nombre': 'Elver',
            'apellido': 'Gomez Torba',
            'email': email,
            'genero': 'Otro',
            'fechanacimiento_birth[day]': '10',
            'fechanacimiento_birth[month]': '10',
            'fechanacimiento_birth[year]': '2001',
            'fechanacimiento_birthDay': '2001-10-10',
            'pais': 'United+States',
            'estado': 'California',
            'ciudad': 'Los+Angeles',
            'celular': phone_number  
        }],

        "coding-problems": ["https://www.dailycodingproblem.com/api2/subscribe", {
            "email": email,
            "referrer":None
        }],
        "mozilla": ["https://basket.mozilla.org/news/subscribe/", {
            "newsletters": "download-firefox-mobile-whatsnew",
            "source-url": "https%3A%2F%2Fwww.mozilla.org%2Fes-ES%2Ffirefox%2F116.0.1%2Fwhatsnew%2F",
            "lang": "es-ES",
            "email": email
        }],
        "church-of-jesus-christ": ["https://account.churchofjesuschrist.org/api/open/accounts",{
            "ageRange":"RANGE_13_PLUS",
            "callerData":'{location: "register"}',
            "location":"register",
            "captcha":"03ADUVZwC0SFId4K3FfcVlwxVi74xrRCIlodYZkCfgzuK_MtyGhjeE4QZH6N8UpZ7rAfpFoyXVPGYvAaRyWu3ttSIV6m1oJryd8NbbYpWa275KNTD53GjcExJRm3R8EezKP-pOO-o5TWjYsgfcwYOT4fJqg2PD2tXwTiU0_gaxwMg6xfIQ5X3LYLeEIXxJfAo_FN2NYswQ2MmHOHFARoekwZUPlhGp3lCIE0JKKgf7FPYIy4ZRztW73y_w54ihZq6kNKgtsOvgzsWFYB7X2VrxZ0ARyilBDSup9FPhjBUF2V8OKjq1lxypf08fsS8KfYIjaTQTKExe2YpwUugtAlcbQ6P5czjg-D6wSDUJy9KbOSqkBZr0KBhLRXCZ0MVjherZuXcmCze6E_5DekgQMmUlgajo8xE_xp7fkR6T27TuJY6nedmY2GJYfwQK16zlZAWWWFCFssneiL1AnnNSSjZI2caSMBV_LcCDJXsyUlcTifRGNs3K2z24IDyZ7ikuv9szaK4hdYrnemwsAmtFc72b6hKZ2y4k4rWOwXSZgo3VAibQVZYvDrKFlODMecgzeIVoHW-NmB6yHSoFpPEF1VV3hPTVA8xBC7Zy1w",
            "countryCode":"CRI",
            "email":email,
            "firstName":"Carlos",
            "lastName":"José",
            "mobilePhone":phone_number,
            "notificationLanguage":"spa",
            "password":"iglesiadedios1",
            "username":"cjmoreno1109"
        }]
    } 
