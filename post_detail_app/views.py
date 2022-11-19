from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from post_detail_app import models
from post_detail_app.models import Comment, Category, Like, DisLike, Post
from post_detail_app import models as post_detail_app_models


def post_detail(request, slug):
    if request.user.is_authenticated:
        comment_sender_profiles = User.objects.all()
        reply_sender_profiles = User.objects.all()
        post_detail_objects = models.Post.objects.get(slug=slug)
        post_detail_objects.how_many_times_clicked += 1
        post_detail_objects.save()
        latest_posts = post_detail_app_models.Post.objects.all().order_by("-updated_at")[:5]
        most_clicked_ones = post_detail_app_models.Post.objects.all().order_by("-how_many_times_clicked")[:5]
        if request.user.likes.filter(post__slug=slug, user_id=request.user.id).exists():
            is_liked = True
        else:
            is_liked = False

        if request.user.dislikes.filter(post__slug=slug, user_id=request.user.id).exists():
            is_disliked = True
        else:
            is_disliked = False

        if request.method == "POST":
            parent_id = request.POST.get("parent_id")
            body = request.POST.get("body")
            if len(request.POST.get("body")) == 0:
                return render(request, "post_detail_app/post.html",
                              context={"post_detail_objects": post_detail_objects, "latest_posts": latest_posts,
                                       "most_clicked_ones": most_clicked_ones,
                                       "error_message": "Your comment can't be empty!",
                                       "is_liked": is_liked, "is_disliked": is_disliked,
                                       "comment_sender_profiles": comment_sender_profiles,
                                       "reply_sender_profiles": reply_sender_profiles})

            if len(request.POST.get("body")) < 1000:
                Comment.objects.create(body=body, post=post_detail_objects, user=request.user, parent_id=parent_id)
                return render(request, "post_detail_app/post.html",
                              context={"post_detail_objects": post_detail_objects, "latest_posts": latest_posts,
                                       "most_clicked_ones": most_clicked_ones,
                                       "is_liked": is_liked, "is_disliked": is_disliked,
                                       "comment_sender_profiles": comment_sender_profiles,
                                       "reply_sender_profiles": reply_sender_profiles})

            else:
                return render(request, "post_detail_app/post.html",
                              context={"post_detail_objects": post_detail_objects, "latest_posts": latest_posts,
                                       "most_clicked_ones": most_clicked_ones,
                                       "error_message": "Your comment has more than 1000 characters!",
                                       "is_liked": is_liked, "is_disliked": is_disliked,
                                       "comment_sender_profiles": comment_sender_profiles,
                                       "reply_sender_profiles": reply_sender_profiles})

        return render(request, "post_detail_app/post.html",
                      context={"post_detail_objects": post_detail_objects, "latest_posts": latest_posts,
                               "most_clicked_ones": most_clicked_ones, "is_liked": is_liked, "is_disliked": is_disliked,
                               "comment_sender_profiles": comment_sender_profiles,
                               "reply_sender_profiles": reply_sender_profiles})

    else:
        return redirect("account_app:join")


def category_detail(request, pk=None):
    category = Category.objects.get(id=pk)
    post_objects = category.post_set.all()
    return render(request, "home_app/index.html", context={"post_objects": post_objects})


def like(request, slug, pk):
    try:
        like = Like.objects.get(post__slug=slug, user_id=request.user.id)
        like.delete()

    except:
        Like.objects.create(post_id=pk, user_id=request.user.id)
        try:
            dislike = DisLike.objects.get(post__slug=slug, user_id=request.user.id)
            dislike.delete()

        except:
            pass

    return redirect("post_detail_app:post_detail", slug)


def dislike(request, slug, pk):
    try:
        dislike = DisLike.objects.get(post__slug=slug, user_id=request.user.id)
        dislike.delete()

    except:
        DisLike.objects.create(post_id=pk, user_id=request.user.id)
        try:
            like = Like.objects.get(post__slug=slug, user_id=request.user.id)
            like.delete()

        except:
            pass

    return redirect("post_detail_app:post_detail", slug)
