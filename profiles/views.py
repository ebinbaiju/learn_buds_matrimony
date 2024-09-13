from django.shortcuts import render
from django.views.generic import TemplateView
#profile display imports :
from django.shortcuts import render, get_object_or_404
from U_auth.models import *
from typing import Any
from django.contrib import messages
from django.http import Http404




# class UserProfileView(TemplateView):
#     template_name = 'users_pr_view.html'

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         user_id = self.kwargs.get('user_id', None)
#         if user_id:
#             user = costume_user.objects.get(id=user_id)
#             user_details = UserPersonalDetails.objects.get(user=user)
#             print(user, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
#             additionalDetails = AdditionalDetails.objects.get(user=user)
#             pictures = Pictures.objects.get(user=user)
#             context['user_details'] = user_details
#             context['additional_details'] = additionalDetails
#             context['pictures'] = pictures
#         messages.error(self.request,"unable to identify user...!!!")
#         return context

class UserProfileView(TemplateView):
    template_name = 'users_pr_view.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id', None)
        
        if user_id:
            try:
                # Get the user object or return 404
                user = get_object_or_404(costume_user, id=user_id)

                # Retrieve related objects safely
                user_details = get_object_or_404(UserPersonalDetails, user_id=user)
                additional_details = get_object_or_404(AdditionalDetails, user=user)
                pictures = Pictures.objects.filter(user=user_details)
              

                # Add retrieved data to the context
                context['user_details'] = user_details
                context['additional_details'] = additional_details
                context['pictures'] = pictures
                context['userinfo'] = user

            except costume_user.DoesNotExist:
                # User not found, set error message and raise a 404
                messages.error(self.request, "User does not exist.")
                raise Http404("User not found")

            except (UserPersonalDetails.DoesNotExist, AdditionalDetails.DoesNotExist, Pictures.DoesNotExist):
                # Related objects not found, set error message and raise a 404
                messages.error(self.request, "Incomplete profile details.")
                raise Http404("Profile details missing")
        else:
            # If user_id is None, raise 404 and display an error message
            messages.error(self.request, "Unable to identify user...!!!")
            raise Http404("User ID not provided")

        return context
    


def messages_pg(request):
    return render(request, 'messages.html')


def user_send_pg(request):
    return render(request, 'send.html')


def user_accept_pg(request):
    return render(request, 'accept.html')


def user_reject_pg(request):
    return render(request, 'reject.html')


def user_recieved_pg(request):
    return render(request, 'recieved.html')

def user_chat_pg(request):
    return render(request, 'col_chat.html')


def user_shortlist_pg(request):
    return render(request, 'shortlist.html')

def user_shortlisted_pg(request):
    return render(request, 'shortlisted_by.html')

def user_contacted_pg(request):
    return render(request, 'contacted.html')

def user_viewed_pg(request):
    return render(request, 'pr_viewed.html')