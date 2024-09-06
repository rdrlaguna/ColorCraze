
document.addEventListener('DOMContentLoaded', function() {

    // Get the nav title element
    const navtitle = document.getElementById('nav-title-link');

    // Get a random number for the hue value
    let hue = Math.floor(Math.random() * 359);;
    setInterval(function(){
        // Changes color in nav title

        // Reset hue value when it's equal to 359
        if (hue === 359) {
            hue = 0;
        }
        // Increase hue by 1
        hue++

        // Change gradient in title text
        navtitle.style.backgroundImage = 
        `linear-gradient(90deg,
            hsl(${hue}, 70%, 60%),
            hsl(${hue + 50}, 70%, 60%))`;
    }, 100)
})


// Function to query the data of the clicked color
function passData(hex_code) {

    // Find the hex code
    const hex = document.getElementById('hex_code');

    // Prepare data to send 
    const data = {
        hex : hex_code,
    }

    // Send data using fetch
    fetch('/colorDetails', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
        },
        body: JSON.stringify(data)
    })

    // Get a response form the server
    .then(response => response.json())
    .then(result => {
        
        // Get the modal, color-container and closing button
        const modal = document.getElementById('myModal');
        const closeBtn = document.getElementById('closeModal');
        
        // .......... Insert The DATA into the modal ..........
        // Style color container
        const colorDisplay = document.getElementById('colorDisplay');
        colorDisplay.style.background = hex_code;

        // Insert color NAME
        const nameContainer = document.getElementById('name-container');
        nameContainer.innerHTML = result["name"]

        // Insert HEX values
        const hexContainer = document.getElementById('hex-container');
        const hexValues = document.createElement('p')
        hexValues.innerHTML = hex_code;
        hexContainer.append(hexValues);

        // Insert RGB values
        const rgb = '(' + result["red"] + ', ' + result["green"] + ', ' + result["blue"] + ')'
        const rgbContainer = document.getElementById('rgb-container');
        const rgbValues = document.createElement('p');
        rgbValues.innerHTML = rgb;
        rgbContainer.append(rgbValues);

        // Insert HSL values
        const hsl = '(' + result["hue"] + 'º, ' + result["saturation"] + '%, ' + result["light"] + '%)'
        const hslContainer = document.getElementById('hsl-container');
        const hslValues = document.createElement('p')
        hslValues.innerHTML = hsl;
        hslContainer.append(hslValues);

        // Insert username inside the modal container
        let submitUser;
        if (result["username"] != 'admin') {
            const modalContainer = document.getElementById('modal-container');
            const submitContainer = document.createElement('div'); 
            submitContainer.className ='submit-container';

            // Capitalize username
            const rawName = result["username"];
            const titleName = rawName.charAt(0).toUpperCase() + rawName.slice(1);

            // Add user name
            submitUser = document.createElement('p');
            submitUser.className = 'modal-username';
            submitUser.innerHTML = 'Submitted by ' + titleName;
            submitContainer.append(submitUser);

            modalContainer.append(submitContainer);
        }

        
        // .......... Open the MODAL ..........
        modal.style.display = "flex";
       
        // Remove inserted data if:
        // User clicks the close button
        closeBtn.onclick = function() {
            closeModal(modal, hexValues, rgbValues, hslValues, submitUser);
        }

        // User clicks outside the modal
        window.onclick = function(event) {
            if (event.target == modal) {
                closeModal(modal, hexValues, rgbValues, hslValues, submitUser);
            }
        }
       
    })
    .catch(error => {
        console.error('Error:', error);
    });

}


function closeModal(modal, hex, rgb, hsl, user){
    // Hide the modal content
    modal.style.display = "none";

    // Remove inserted values
    hex.remove();
    rgb.remove();
    hsl.remove();

    if (user != undefined) {
        user.remove();
    }

}

// TODO: Change color of title every 30 seconds based on color of datbase.
// query databaase for all hex
// create a timer
// change color every x seconds

// Function to change the hue values on nav title
function changeHue(hue) {
    if (hue === '359') {
        hue = 0;
    }

    hue++

    console.log(hue);
}


// .......... T O P    F U N C T I O N S ..........

// Show color in slides
function showSlides(n) {
    let i;
    let dots = document.getElementsByClassName('dot-select');
    
    const slide = document.getElementById('s-box');
    const number = document.getElementById('s-number');
    const votes = document.getElementById('s-votes');
    const name = document.getElementById('s-name');    

    // Clear active class from all dots
    for (i = 0; i < dots.length; i++) {
        dots[i].classList.remove('active');
    }

    // Insert data in slide 
    slide.style.backgroundColor = hexList[n];
    name.innerHTML = nameList[n];
    votes.innerHTML = votesList[n] + ' votes';
    number.innerHTML = `${n + 1} / 3`;

    console.log(lightList[n]);
    // Change text color depending lightness
    if (lightList[n] <= 70) {
        slide.classList.remove('top-dark-name');
        slide.classList.add('top-light-name');
    } else {
        slide.classList.remove('top-light-name');
        slide.classList.add('top-dark-name');
    }

    // Highlight corresponding dot
    dots[n].classList.add('active');
}

// Change slide index clicking Next / Prev buttons
function moveSlides(id) {

    // User clicks Prev
    if(id === 'prev') {
        if (slideIndex === 0) {
            slideIndex = 2;
        } else {
            slideIndex -= 1;
        }
    // User clicks Next
    } else {
        if (slideIndex === 2) {
            slideIndex = 0
        } else {
            slideIndex += 1;
        } 
    }

    // Show selected slide
    showSlides(slideIndex);
}

// Change slide when clicking dot buttons
function currentSlide(n) {
    showSlides(slideIndex = n)
}