from . import models


def get_company_details(request):
    company = models.Company.objects.first()
    address = models.Address.objects.filter(address_type='p').first()
    footer = models.Footer.objects.all().first()
    if company:
        return {
            'company': company,
            'address': address,
            'footer': footer,
        }
    else:
        return {
            'company': None,
            'address': None,
            'footer': None,
        }
