### Conceptual Exercise ###

__Answer the following questions below:__

* What are important differences between Python and JavaScript?

>_Python is typically executed on the server-side, while JavaScript is executed on the client-side in web browsers, and on the server-side with Node.js._
>_Python has a clear and simple syntax that makes it easy to learn and read, while JavaScript has a more complex and verbose syntax. Python uses indentation to indicate blocks of code, while JavaScript uses braces {}._
>_Python is commonly used for scientific computing, data analysis, and artificial intelligence, while JavaScript is mainly used for building web applications, interactive front-end development, and server-side programming with Node.js._

* Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") without your programming crashing.

>_Method1: We use get(x, default) function to return the default value for the key "c"._
    print({"a": 1, "b": 2}.get("c", 3)) 

>_Method2_: Adding the value for c, so the dictionary will get new key_value and add it at the end of itself_
    my_dict = {"a": 1, "b": 2}
	try:
		value = my_dict["c"]  
	except KeyError:
		value = 3  
  
* What is a unit test? 
>_A unit test is a type of software testing that verifies the individual components or "units" of a software application are working correctly as designed._

* What is an integration test?
>_An integration test is a type of software testing that verifies the interactions and behavior between different components or modules of a software application. In other words, an integration test ensures that the integrated system works as expected when its individual components are combined and interact with each other._

* What is the role of web application framework, like Flask?
>_Flask is to provide a standardized set of tools and conventions for building web applications, allowing developers to focus on the unique features and logic of their application rather than the low-level details of web development._ 

* You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?
>_Route parameters are better suited for identifying specific resources or pages in your application, while Query parameters are better suited for providing additional information or filters._

* How do you collect data from a URL placeholder parameter using Flask?
>_You can collect data from a URL placeholder parameter by defining a route with a placeholder parameter in the route pattern, and then defining a function that takes an argument with the same name as the placeholder parameter.._

* How do you collect data from the query string using Flask?
>_Using 'request.args.get()'._

* How do you collect data from the body of the request using Flask?
>_Use request.form to get the name attribute of element from the form in HTML which submitted by POST method and send along with the request in the body_

* What is a cookie and what kinds of things are they commonly used for?
>_A cookie is a small piece of data that a website stores on a user's computer or mobile device. Cookies are sent by a website to a user's web browser and are stored on the user's device. Cookies are commonly used to store information about the user's preferences and activity on the website._

* What is the session object in Flask?
>_In Flask, the session object is a dictionary-like object that allows you to store data across multiple requests from the same client. The session object uses cookies to store data on the client side, and the data is encrypted to prevent tampering._ 

* What does Flask's `jsonify()` do?
>_Flask's jsonify() function is a helper method that serializes data into JSON format and sets the response headers to indicate that the response should be treated as JSON data._
