from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from django.urls import reverse
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
import base64


# Create your views here.
# def bokehView(request):

#     #Graph X & Y coordinates
#     x=[1,2,3,4,5,6,7]
#     y=[1,2,3,4,5,6,7]

#     #Setup graph plot for displaying line graph
#     plot=figure(title='Language Trends', x_axis_label="Programming Language", y_axis_label="Frequency", width=400, height=400)

#     #plot line
#     plot.line(x,y, line_width=2)

#     #store components
#     script, div=components(plot)
#     #plot_json=json.dumps(json_item(plot))

#     #return to display page with components sent as arguments which will then be displayed
    
#     return render(request, 'histogramApp/plot_display.html', {'script':script, 'div':div})
#     #return render(request,'histogramApp:plot_display.html', {'plot_json':plot_json})
#     # return render(request, 'histogramApp/plot_display.html', {
#     #     'script': script,
#     #     'div': div,
#     #     'url': reverse('histogramApp:histogram_url')
#     # })


def bokehView(request):

    # Sample data (replace with your actual data)
    data = [1, 2, 3, 2, 4, 5, 1, 3, 4, 2]

    # Create histogram using matplotlib
    plt.figure(figsize=(7, 5))  # Customize plot size as needed
    plt.hist(data, bins=10, edgecolor='black', color='blue', alpha=0.7)  # Set histogram parameters
    plt.xlabel('Programming Languages')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.grid(True)  # Optional: Add gridlines for better readability

    # Create a byte buffer for the image
    

    # Save the plot as a PNG image (adjust the file format if needed)
    #plt.savefig(buffer, format='png')
    
    # with open('histogram.png','wb') as f:
    #     f.write(buffer.getvalue())

    # with open('histogram.png','rb') as f:
    #     image_data=base64.b64encode(f.read()).decode('utf-8')
    # context={'plot_image':image_data}


    # Clear the plot for future use (optional)
    #plt.clf()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_data=base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Set the content type and return the image as a response
    # response = HttpResponse(buffer.getvalue(), content_type='image/png')
    # return response
    
    #context = {'plot_image': buffer.getvalue()}  # Add image data to context
    context= {'plot_image':image_data}
    plt.clf()
    return render(request, 'histogramApp/plot_display.html', context)