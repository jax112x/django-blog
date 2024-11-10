from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "life-of-a-feline",
        "image": "winkie.jpeg",
        "author": "Kit Cat",
        "date": date(2023, 5, 14),
        "title": "The Secret Life of a Feline",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "content": """
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. 
          Cras venenatis euismod malesuada. Nullam ac erat et orci tincidunt tristique non vel arcu. Quisque malesuada 
          justo sit amet metus bibendum, sit amet cursus urna vestibulum. Fusce id facilisis lectus. Nullam sit amet 
          justo nisi. Integer laoreet, orci non interdum venenatis, eros lectus pulvinar magna, at interdum risus nisi ac odio.

          Suspendisse potenti. Nam ut magna lectus. Nulla facilisi. Praesent ultricies nulla nisl, sit amet consequat est 
          vehicula eu. Nullam ut justo eu lorem fermentum scelerisque ac vel nulla. Mauris vitae magna at diam fermentum 
          sodales et et dolor.
        """
    },
    {
        "slug": "the-art-of-purring",
        "image": "truffs.jpeg",
        "author": "Kit Cat",
        "date": date(2023, 9, 1),
        "title": "The Art of Purring",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "content": """
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vulputate tincidunt ex, at aliquet libero consequat a. 
          Nulla volutpat tincidunt ornare. In hac habitasse platea dictumst. Pellentesque viverra, ex in fringilla cursus, 
          neque lorem dapibus arcu, eget cursus sem sapien et est.

          Cras in purus eget nunc egestas porttitor. Sed vitae tincidunt nisl, sed volutpat enim. Praesent euismod sapien 
          nulla, ut euismod purus fermentum at. Sed eget turpis vel elit dictum egestas. Curabitur varius, sapien quis 
          venenatis dignissim, felis eros vehicula sem, a posuere massa ligula eget arcu.
        """
    },
    {
        "slug": "chasing-lasers",
        "image": "penny.jpeg",
        "author": "Kit Cat",
        "date": date(2023, 12, 10),
        "title": "Chasing Lasers: A Cat's Endless Quest",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "content": """
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas fringilla malesuada quam non venenatis. 
          Ut bibendum tortor sit amet tellus aliquet, sed dignissim felis commodo. Vivamus non risus nulla. Quisque 
          fermentum posuere justo, nec luctus velit scelerisque eget.

          Donec quis orci id nibh lacinia sollicitudin. Nulla facilisi. Etiam venenatis risus sit amet sapien tincidunt, 
          nec ultricies nulla consequat. Integer convallis lacinia risus, vel congue mi. Praesent id erat at enim 
          porttitor tempor. Curabitur vulputate ultricies massa nec accumsan.
        """
    }
]

def get_date(post):
    return post['date']
    
def index(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request,"blog/index.html",{
        "posts" : latest_posts
    })

def posts(request):
    sorted_posts = sorted(all_posts,key=get_date)
    return render(request,"blog/posts.html",{
        "posts" : sorted_posts
    })

def post_details(request,slug):
    current_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post_details.html",{
        "post" : current_post
    })
