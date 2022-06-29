<h1> Reset Bali  </h1>

<h3> Full stack project - PP4 </h3>

The RESET BALI application showcases an "oasis of peace" in the form of three wellness programmes. The programmes consist of a number of activities including yoga, meditation and guided hikes. 


<h1> User Experience (UX) </h1>

<h2> User Stories </h2>

 - As a first time user, I want to easily navigate the site.
 - As a first time user, I want to be informed about the different programmes on offer.
 - As a first time user, I want to read testimonials from previous customers.
 - As a first time user, I want to register an account on the site.

- As a returning user, I want to log into my account.
- As a returning user, I want to reserve a spot on an upcoming program.
- As a returning user, I want to be able to contact the company.
- As a returning user, I want to submit a review.
 

<h2> The Strategy Plane </h2>

Reset Bali is a web application that informs the user of a wellness retreat based in two locations in Bali. The user can choose between the two locations, each location offering a different program, the reset, rewind and renew program. The user will be able to create an account, read reviews left by previous attendees and also book their slot in an upcoming programme of their choice. 


<h2> The Scope Plane </h2>

While planning the site design, I wanted to ensure the user could navigate easily throughout the site and to know where they are. I plan for the site to be bright and simple but also interactive to ensure a positive user experience. The testimonial section will give the user insight to what is on offer, giving them confidence in the service.

<h2> The Structure Plane </h2>

Upon visting the site, the user will first see a striking hero image that depicts the theme of the site. Below the image, the user will get a little synopsis of what to expect from 'Reset Bali', followed by some detailed information to further inform the user. Near the end of the home page, the user will be able to view testimonials and past attendees will also be able to post reviews to the site. The Nav bar contains three sections, a link to the home page, the programmes page and a contact page. 

Once the user clicks on the link to the programmes, two locations will appear. The user can then choose the location of choice and the available programmes at that location will appear. The user can then then find more information on each programme and also have the option to see availability and book a space. Pricing will also be displayed.

The Contact page will contain a standard 'contact us' form for the user to reach out if needed. Phone and email details aswell as the two locations are detailed to the user.

<h2> The Skeleton Plane </h2>

<h3> Home page </h3>

![home](readme/images/home-page.png)

<h3> locations and programmes </h3>

![](readme/images/program-locations.png)

![](readme/images/ubud.png)

![](readme/images/seminyak.png)

<h3> Reservations </h3>

![](readme/images/reservations.png)

<h3> Contact us </h3>

![](readme/images/contact-page.png)

![](readme/images/modal.png)


<h3> Models </h3>

<h4> Database </h4>

I will use a PostGreSQL database for the project.

<h4> Review model </h4>

KEY

title,    
date, 
program, 
user, 
review, 
rating


<h4> Calender/booking model </h4>

KEY

user, 
email_address, 
phone, 
date, 
programme, 
number_of_spaces
