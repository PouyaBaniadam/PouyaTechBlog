from django.shortcuts import render, redirect

from add_post_app.forms import AddPostForm
from post_detail_app.models import Post


def add_post(request):
    if request.user.is_anonymous:
        return redirect('account_app:join')
    add_post_form = AddPostForm()

    if request.method == "POST":
        author = request.user
        add_post_form = AddPostForm(request.POST, request.FILES)
        if add_post_form.is_valid():
            instanse = add_post_form.save()
            instanse.author = author
            instanse.how_many_times_clicked = 0
            instanse.save()
            success_message = "Post has been sent successfully. It'll be uploaded after a while ... ⌚"
            return render(request, "add_post_app/add_post.html",
                          context={"add_post_form": add_post_form, "success_message": success_message})

    return render(request, "add_post_app/add_post.html", context={"add_post_form": add_post_form})
