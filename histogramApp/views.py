from django.shortcuts import render
# from bokeh.plotting import figure, output_file, show
# from bokeh.embed import components
from django.urls import reverse
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
import base64
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

#section for the tags
from taggit.models import TaggedItem #importing the Tag model from Taggit sub inbuilt app



def histogramDisplay(request):

    #collect tags and their frequencies across both apps
    tagged_items=TaggedItem.objects.select_related('tag').annotate(count=models.Count('tag'))
    #filteriing by content-type for QuestionClass and PostApp
    tagged_items=tagged_items.filter(content_type__model__in=['QuestionClass','PostClass'])

    #extracting data for plotting
    tags=[item.tag.name for item in tagged_items]
    counts=[item.count for item in tagged_items]


    # Create histogram using matplotlib
    plt.figure(figsize=(7, 5))  # Customizing plot size as needed
    plt.hist(tags, bins=10, edgecolor='black', color='blue', alpha=0.7)  # Set histogram parameters
    plt.xlabel('Programming Languages')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.grid(True)  # Optional: Add gridlines for better readability

    
    # Create a byte buffer for the image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_data=base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    
    #context = {'plot_image': buffer.getvalue()}  # Add image data to context
    context= {'plot_image':image_data}
    plt.clf()
    return render(request, 'histogramApp/plot_display.html', context)