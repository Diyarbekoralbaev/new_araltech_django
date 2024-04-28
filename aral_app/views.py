from django.shortcuts import render
from .models import AboutModel, OurPartnersModel, ServicesModel, TestimonialModel, PortfolioModel, \
    TeamMembersModel, FaqModel, BlogModel, ContactModel, AwardsModel, ProjectCategoryModel, BlogCategoryModel


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


def custom_404(request):
    return render(request, '404.html', status=404)