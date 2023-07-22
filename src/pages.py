from typing import Any, Dict, List, Union

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
        "united-nations-news": ["", {
        "u": "372753f560ef60c400f1a4f3f",
        "id": "fdbf1af606",
        "c": "jQuery19009144254332436061_1690067228881",
        "EMAIL": email,
        "FNAME": "John ",
        "LNAME": "Denver",
        "OCCUPATION": "Other",
        "AGE": "20-30",
        "group[577][1]": "1",
        "group[577][2]": "2",
        "group[577][4]": "4",
        "group[577][256]": "256",
        "group[577][512]": "512",
        "group[577][8]": "8",
        "group[577][1024]": "1024",
        "group[577][2048]": "2048",
        "group[577][4096]": "4096",
        "group[577][8192]": "8192",
        "group[577][16]": "16",
        "group[577][16384]": "16384",
        "group[673][32]": "32",
        "group[673][64]": "64",
        "group[673][128]": "128",
        "group[673][32768]": "32768",
        "EMAILTYPE": "html",
        "b_372753f560ef60c400f1a4f3f_fdbf1af606": "",
        "subscribe": "Subscribe",
        "_": "1690067228882",
        }
        ],
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

        "peruquiosco": ["https://id.tinypass.com/id/api/v1/identity/register/token?aid=pWgh0wFvpu&lang=es_PE&tbc={kpex}DfkoOBY3eLouEav7NQJ18RqO0qv5bxTWnO2JCC_8CDIQwPXvpzhEMD3YspZZwjPE", {
            "first_name": "Elver",
            "last_name": "Gonmez",
            "email": email,
            "password": "peneduro22",
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
            "new_password": "MikaelYordan666_",
            "confirm_password": "MikaelYordan666_",
            "month": "09",
            "day": "17",
            "year": "1996"
        }],
        "quora": ["https://es.quora.com/graphql/gql_POST?q=SignupEmailBasicInfoModal_sendSignupEmailConfirmationEmail_Mutation", {
            "email": email
        }]
    }