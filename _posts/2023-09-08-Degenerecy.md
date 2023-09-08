---
toc: false
comments: false
layout: post
author: Tirth Thakkar, Haseeb Beg (Degenerate Code Monkey)
title: Javascript!!
description: Javascript Checkout
type: tangibles
courses: { compsci: {week: 2} }
---
<style>
body {
    margin: 0;
    background: linear-gradient(-45deg, pink, rgb(231, 110, 150), pink, rgb(243, 108, 176), pink, rgb(223, 116, 134), pink, rgb(156, 90, 117), pink);
    background-size: 400% 400%;
    animation: gradientChange 5s linear infinite;
    background-repeat: no-repeat; /* Prevents a jump when the animation restarts */
    background-color: pink; /* Matches the initial gradient color */
}

@keyframes gradientChange {
    0% {
        background-position: 0% 0%;
    }
    100% {
        background-position: 100% 100%;
    }
}


    .page-description{
        color: black !important;
        font-family: cursive !important;
    }

    .post{
        color: black !important;
        font-family: cursive !important;
    }
    .post-header{
        /* making a rainbow gradient for the header color */
        color: black !important;
        font-family: cursive;
    }
    .p-author{
        color: black !important;
    }
    .dt-published{
        color: black !important;
    }

    .read-time{
        color: black !important;
    }
    .page-content{
        color: black !important;
    }
    .site-header {
        background-color: #ff00ff !important;
        background-image: url("https://www.freecodecamp.org/news/content/images/size/w2000/2021/06/w-qjCHPZbeXCQ-unsplash.jpg") !important ;
    }
    .site-nav{
        background-color: #ff00ff !important;
        background-image: url("https://www.freecodecamp.org/news/content/images/size/w2000/2021/06/w-qjCHPZbeXCQ-unsplash.jpg") !important ;
        opacity: 0;
    }
    h2 {
        font-size: 1.5em;
        font-weight: normal;
        font-family: cursive;
    }

    .wrapper{
        color: black !important;
    }

    #image-container img {
        min-width: 45%;
        max-width: 100%;
        border-radius: 10px; /* Add rounded corners */
    }

    #image-container {
        align-items: left;
        text-align: left; /* Align images to the left */
        padding: 10px; /* Add padding around the image */
    }

    #horny{
        background-image: url("https://www.freecodecamp.org/news/content/images/size/w2000/2021/06/w-qjCHPZbeXCQ-unsplash.jpg") !important ;
    }
</style>
<head>
    <meta charset="UTF-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Fetch API Image Example</title>
</head>
<body>
    <h2>UWU wwelcome twoglodytes basement duwuellers</h2> <button id = "horny">New Waifu</button>
    <div id="image-container"></div>
    <script>
        function GetWaifu() {
            const settings = {
                async: true,
                crossDomain: true,
                url: 'https://any-anime.p.rapidapi.com/anime/gif',
                method: 'GET',
                headers: {
                    'X-RapidAPI-Key': '0588371053msha6940727d7c83aap107c98jsn19374300bf1d',
                    'X-RapidAPI-Host': 'any-anime.p.rapidapi.com'
                }
            };

            $.ajax(settings)
                .done(function (response) {
                    if (response.indexOf('<img') !== -1) {
                        // Create a temporary container element to hold the HTML response
                        var tempContainer = document.createElement('div');
                        tempContainer.innerHTML = response;

                        // Find the image element within the temporary container
                        var imgElement = tempContainer.querySelector('img');

                        if (imgElement) {
                            var animeURL = imgElement.getAttribute('src');
                            var image = document.createElement('img');
                            image.src = animeURL;
                            var imageContainer = document.getElementById('image-container');
                            imageContainer.innerHTML = ''; // Clear previous images
                            imageContainer.appendChild(image);
                        } else {
                            console.error("No image found in HTML response.");
                        }
                    } else {
                        console.error("Invalid HTML response:", response);
                    }
                });

        }

        function Uwuification(){
            const url = "https://waifu.it/api/uwuify";
            const text = "Hello world"; // Replace with your desired uwuify length (optional).
            const accessToken = "YOUR_ACCESS_TOKEN"; // Replace with your actual access token.

            const requestData = {
                text: text || undefined,
            };

        $.ajax({
            url: url,
            method: "GET",
        headers: {
            Authorization: accessToken,
        },
        data: requestData,
        success: function (data) {
            console.log(data);
        },
        error: function (xhr, status, error) {
            console.error(error);
        },
    });

        }

        var button = document.getElementById('horny');
        // Attach the click event listener to the button
        // Calling GetWaifu() every 10 seconds automatically 
        GetWaifu();
        setInterval(GetWaifu, 15000);

        button.addEventListener('click', GetWaifu);
    </script>
</body>

