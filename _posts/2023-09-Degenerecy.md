---
toc: true
comments: false
layout: post
title: Javascript Checkout Assignment with Image APIs
description: Javascript Checkout 
type: hacks
courses: { compsci: {week: 3} }
---
  <head>
    <meta charset="UTF-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Fetch API Image Example</title>
  </head>
  <body>
    <h1>Fetch API Image Example</h1>
    <button id="fetch-image-button">~click me uwu~</button>
    <div id="image-container"></div>
    <script>
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
        $.ajax(settings).done(function (response) {
                console.log(response);
            });
        var button = document.getElementById('fetch-image-button');
            // Attach the click event listener to the button
        button.onclick = function() {
                settings(); // Call the function when the button is clicked
            }
    </script>
</body>







