from django.shortcuts import render, redirect
from .models import AboutModel, OurPartnersModel, ServicesModel, TestimonialModel, PortfolioModel, \
    TeamMembersModel, FaqModel, BlogModel, ContactModel, AwardsModel, ProjectCategoryModel, BlogCategoryModel
from .forms import ContactForm
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.conf import settings


@cache_page(settings.CACHE_TTL)
def home(request):
    about = AboutModel.objects.first()
    partners = OurPartnersModel.objects.all()
    services = ServicesModel.objects.all()
    testimonials = TestimonialModel.objects.all()
    portfolios = PortfolioModel.objects.all()
    team = TeamMembersModel.objects.all()
    faqs = FaqModel.objects.all()
    blogs = BlogModel.objects.all()
    awards = AwardsModel.objects.all()
    portfolio_categories = ProjectCategoryModel.objects.all()

    context = {
        'about': about,
        'partners': partners,
        'services': services,
        'testimonials': testimonials,
        'portfolios': portfolios,
        'team': team,
        'faqs': faqs,
        'blogs': blogs,
        'awards': awards,
        'portfolio_categories': portfolio_categories,
    }

    return render(request, 'index.html', context)


@cache_page(settings.CACHE_TTL)
def blog_detail(request, id):
    blog = BlogModel.objects.get(id=id)
    recent_blogs = BlogModel.objects.exclude(id=id).order_by('-created_at')[:3]
    categories = BlogCategoryModel.objects.all()
    context = {
        'blog': blog,
        'categories': categories,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'blog-details.html', context)


@cache_page(settings.CACHE_TTL)
def project_details(request, id):
    project = PortfolioModel.objects.get(id=id)
    recent_projects = PortfolioModel.objects.exclude(id=id).order_by('-created_at')[:3]
    categories = ProjectCategoryModel.objects.all()
    context = {
        'project': project,
        'categories': categories,
        'recent_projects': recent_projects,
    }
    return render(request, 'portfolio-details.html', context)


@cache_page(settings.CACHE_TTL)
def custom_404(request):
    return render(request, '404.html', status=404)


@cache_page(settings.CACHE_TTL)
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the success page after form is successfully saved
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
