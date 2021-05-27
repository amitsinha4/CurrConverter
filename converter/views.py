"""
Views Module of converter
"""
from django.views.generic import TemplateView, View
from forex_python.converter import CurrencyRates
from converter.models import CurrencyList
from django.http import JsonResponse


class HomePage(TemplateView):
    """ Home Page """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currency_list'] = CurrencyList.objects.filter(is_active=True)
        return context


class TestPage(View):
    """
    Test Page
    """

    def get(self, request):
        """
        Get request
        """
        return JsonResponse({"status": "Success"})


class ConvertView(View):
    """ Converting currency view """
    __curr = CurrencyRates()

    def get(self, request):
        """ Get Reuqest """
        try:
            curr_val = request.GET.get('curr_val')
            curr_val = float(curr_val)
            from_curr = request.GET.get('from_curr')
            to_curr = request.GET.get('to_curr')
            rate = self.__curr.get_rate(from_curr, to_curr)
            final_val = round(curr_val * rate, 2)
            return JsonResponse(
                {"status": "success", "converted_value": final_val}
            )
        except ValueError:
            return JsonResponse(
                {"status": "error", "msg": "Either supplied value is not a valid currency or the field is empty"}
            )
        except Exception as e:
            return JsonResponse({"status": "error", "msg": str(e)})
