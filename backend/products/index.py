from . models import Product
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = ['title',
    'contenst',
    'price',
    'user',
    'public'
    ]
    settings = {
        'attributesForFaceting':['user','public'],
        'searchableAttributes':['title','contenst']
    }
    tags = 'get_tags_list'