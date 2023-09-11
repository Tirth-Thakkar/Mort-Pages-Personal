---
toc: false
comments: false
layout: post
author: Tirth Thakkar, Haseeb Beg (Degenerate Code Monkey)
title: Javascript!!
description: Javascript Checkout
type: tangibles
courses: { compsci: {week: 3} }
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

    form{
        background: none;
        align-items: inline;
    }
    .form-container {
        display: flex; /* Make its children inline */
        align-items: center; /* Vertically center the form elements */
    }

    /* Apply styles to the form elements */
    #Owoification {
        background: none;
        background-color: white !important;
        border: 2px solid black;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
        font-family: cursive;
        margin-right: 10px; /* Add some spacing between the input and button */
    }

    #output-container, #ye{
        background: none;
        background-color: #323443 !important;
        border: 2px solid white;
        color: white;
        margin: 10px;
        border-radius: 10px;
        min-width: 40px;
        padding: 10px;
        font-family: cursive;
        margin-right: 10px; /* Add some spacing between the input and button */
    }

    #owo {
        background-image: url("https://www.freecodecamp.org/news/content/images/size/w2000/2021/06/w-qjCHPZbeXCQ-unsplash.jpg") !important;
        border: 2px solid black;
        color: white;
        font-family: cursive;
        cursor: pointer; /* Change cursor to pointer for the button */
    }
    input[type=text]{
        color: black !important;
        font-family: cursive !important;
    }

</style>
<head>
    <meta charset="UTF-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js">import axios from "axios";</script>
    <title>Fetch API Image Example</title>
</head>
<body>
    <h2>UWU wwelcome twoglodytes bawaesment duwuewers</h2>
    <button id="horny">New Waifu</button>
    <div id="image-container"></div>
    <!-- Wrap the form elements in a container -->
    <div class="form-container">
        <input type="text" id="Owoification" placeholder="Owoify me daddy">
        <input id="owo" type="submit" value="Submit">
    </div>
    <div id="output-container" class="rounded-box">Output will be here.</div>
    <h2>KANYE REST</h2>
    <h3 id="ye"></h3>
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
                        let tempContainer = document.createElement('div');
                        tempContainer.innerHTML = response;

                        // Find the image element within the temporary container
                        let imgElement = tempContainer.querySelector('img');

                        if (imgElement) {
                            let animeURL = imgElement.getAttribute('src');
                            let image = document.createElement('img');
                            image.src = animeURL;
                            let imageContainer = document.getElementById('image-container');
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

        function Uwuification() {
            const url = "https://waifu.it/api/owoify";
            const text = document.getElementById("Owoification").value;
            const outputContainer = document.getElementById("output-container");

        axios
            .get(url, {
                headers: {
                    Authorization: "NjM4NDQ4NzMyNjA1Nzc1ODky.MTY5NDE1MDU5OA--.64621169e9",
                },
                params: {
                    text: text || undefined,
                },
            })
            .then((response) => {
                const textValue = response.data.text; // Extract the "text" property
                outputContainer.textContent = textValue;
            })
            .catch((error) => {
                console.error(error);
                outputContainer.textContent = "Error: " + error.message; // Display an error message if the request fails
            });
        }

            function getQuote(){
                $(document).ready(function(){
                    const grab = $.get("https://api.kanye.rest", function(result){
                        const quote = result.quote;
                        document.getElementById("ye").innerHTML=quote;
                        var msg = new SpeechSynthesisUtterance();
                        msg.text=quote;
                        msg.rate = 1.75;
                        window.speechSynthesis.speak(msg);
                    });
                    });
                }



        let button = document.getElementById('horny');
        let owo = document.getElementById('owo');
        // Attach the click event listener to the button
        // Calling GetWaifu() every 10 seconds automatically 
        GetWaifu();
        setInterval(GetWaifu, 15000);
        owo.addEventListener('click', Uwuification);
        button.addEventListener('click', GetWaifu);
        getQuote();
        setInterval(getQuote, 10000);
    </script>
</body>

