from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'DJANGO',
        'author': 'Asoo',
        'image': 'python.png',
        'date': date(2021, 4, 5),
        'abstract': 'This is DJANGO',
        'content': """
                Lorem ipsum dolor sit amet, conslorum ducimus ea
            est et incidunt libero magnam molestiae molestias nulla, officiis recusandae rem unde vero? Ad aperiam
            asperiores beatae blanditiis, consequatur consequuntur cumque distinctio et eum ex, fuga fugiat illum,
            
        """

    },

    {
        'slug': 'learning-cakes',
        'title': 'cakes',
        'author': 'Mahshid',
        'image': 'images.png',
        'date': date(2022, 3, 6),
        'abstract': 'This is cake',
        'content': """
                Lorem ipsum dolor sit amet,ate dolorum ducimus ea
            est et incidunt libero magnam molestiae molestias nulla, officiis recusandae rem unde vero? Ad aperiam
            asperiores beatae blanditiis, consequatur consequuntur cumque distinctio et eum ex, fuga fugiat illum,
            incidunt iusto magnam modi nemo numquam officia placeat provident quaerat quas ratione repellat sint tempora
            vel vitae.
        """

    }, {
        'slug': 'learning-master',
        'title': 'MASTER',
        'author': 'Marmar',
        'image': 'master.jpg',
        'date': date(2021, 3, 5),
        'abstract': 'This is master',
        'content': """
                Lorem ipsum d elit. Aliquid atque cumque cupiditate dolorum ducimus ea
            est et incidunt libers recusandae rem unde vero? Ad aperiam
            asperiores beatae blanditiis, consequatur consequuntur cumque distinctio et eum ex, fuga fugiat illum,
            incidunt iusto magnam modi nemo numquam officia placeat provident quaerat quas ratione repellat sint tempora
            vel vitae.
        """

    }, {
        'slug': 'learning-ml',
        'title': 'ML',
        'author': 'Azar',
        'image': 'ml.png',
        'date': date(2021, 4, 3),
        'abstract': 'This is ML',
        'content': """
                Lorem ipsum dolor sit d atque cumque cupiditate dolorum ducimus ea
            est et incidunt libero magnam molestiae molestias nulla, officiis recusandae rem unde vero? Ad aperiam
            asperiores beatae blanditiis, consequatur consequuntur cumque distinctio et eum ex, fuga fugiat illum,
            incidunt iusto magnam modi nemo numquam officia placeat provident quaerat quas ratione repellat sint tempora
            vel vitae.
        """

    }

]


def getDate(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=getDate)
    latest_post = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'latest_post': latest_post})


def posts(request):
    context = {
        'allPosts': all_posts
    }
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post

    })
