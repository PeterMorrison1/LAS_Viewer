# LAS_Viewer

This project was intended to be a weekend project to determine the capabilities of Streamlit for making quick applications to demo Data Sceince/Analytics & Data Engineering projects. I chose to use Log ASCII Standard (LAS) files as the initial test since it was relatively simple data (unlike my other project with baby names, which was marginally more complex) and there aren't too many web-based viewers for LAS Files. As mentioned earlier, it was inteded to be a weekend project but I believe this small demo took only an hour (as its not intended to be a production product, just a demo of Streamlit).

[View the live application by clicking this link](https://share.streamlit.io/petermorrison1/las_viewer/main/main.py)

## Explaining the Project
The goals were:
1. Display LAS Data
    * In the "Summary" section you can view the header info, parameters, and the raw data points
2. Visualize Raw LAS Data Points
    * You can create your own chart in the "Build a Custom Chart" section which lets you choose what type of chart (line or histogram only), the x-axis, y-axis, and you can select multiple parameters
3. Show that Streamlit apps can receive parameters via URL params
    * This was to show that you could pass a file name or id as a part of the URL and the app could send a request to a server or file system to get the LAS file. I don't want to host a server for this and only found one LAS file to demo the project, so I stopped at having the "Query params: ${}" which will populate if you use a URL parameter like [this link here](https://share.streamlit.io/petermorrison1/las_viewer/main/main.py?paramtest=hi)
4. Show that Streamlit apps can receive file uploads
    * The built in file upload/download system from Streamlit is extremely easy to use and didn't require much additional effort. 

## Other Info
* I used the [lasio library](https://lasio.readthedocs.io/en/latest/) to parse the LAS files which simply output them to a Pandas dataframe, making it _extremely_ simple to get this project working in an hour. 
* There was another Streamlit app on the demo page that reads LAS files, I didn't notice this until I was nearly done but I learned some formatting/design (sidebar, layout) concepts on Streamlit from it. Unliek this project it not a demo, please check it out if you need to visualize LAS files [at this link](https://github.com/andymcdgeo/las_explorer)
* The example LAS file was from [Minnelusa Digital Well Log Data](www.Minnelusa.com) which can be contacted at [info@Minnelusa.com](info@Minnelusa.com)
