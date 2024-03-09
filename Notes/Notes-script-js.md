# Script.js
```$(document).ready(function() {}```
- This portion runs whatever is enclosed in its brackets once the document is fully loaded
- This allows more **efficient** & **consistent** load time
- In the code, nothing will run untul the document is ready


### The toggleInoutField() Function
- Because the Web App has <u>Two Basic Functionalities</u> (inserting a url or inserting a description), we want to create a function to easily handle both
- <u>The purpose of this function</u> is to be able to adjust how the code handles the inputs based on the dropdown menu option

```
if (inputType === 'url') {
    $('#inputValue').attr('placeholder', 'Enter URL').attr('type', 'url').css('height', '100px');
    $('#inputLabel').text('Enter URL:');
}
```
- If the input value is ```'url'```, then it will do multiple things at once
1. for any elment with the id of ```'inputValue'```, change its attributes accordingly.
2. for any element with the id of ```'inputLabel'```, change its text.

```
else if (inputType === 'description') {
$('#inputValue').attr('placeholder', 'Enter Product Description').attr('type', 'text').css('height', '200px');
$('#inputLabel').text('Enter Product Description:');
}
```
- else, if the input value is ```'description'```, then do the same things as above with a different format

Finally, we have this line of code at the end ```$('#inputValue').val('');``` so that after performing an action, it will clear the input to make a clean state

#### Side Note
The ```$``` symbol is a JQuery Library shorthand. It simplifies the process of manipulating HTML documents, handling events, creating animations, and making AJAX requests.

### Once the page Loads
```toggleInputField();``` This ensures that the input field is initially set based on the default values of the dropdown

``` $('#inputType').change(function() {toggleInputField();});``` This sets up an event listener for the dropdown with the id inputType. When the value of the dropdown changes (i.e., when the user selects a different option), the provided function is executed. In this case, it calls the toggleInputField function.

### Event Handler
```$('#keywordForm').submit(function(event) {``` Sets up an event handler to capture the form submission event for the form with the id keywordForm. The provided function ensures that the form is not submitted in the traditional way, and it defines the logic for handling the form submission asynchronously through AJAX.

1. **Form Submission Event:**

In HTML, a form submission event occurs when a user interacts with a form (e.g., clicks a submit button). When this event is triggered, the browser initiates the process of sending the form data to the server for processing.

2. **Traditional Form Submission:**

In the traditional way, when a user submits a form, the browser navigates to a new page or reloads the current page. This is known as a full-page reload. The entire content of the page is replaced with the response from the server.

3. **Event Handler:**

An event handler is a piece of code (usually a function) that gets executed in response to a specific event. In this case, the event handler is set up to capture the form submission event.

4. **Preventing Default Behavior:**

event.preventDefault(); is used to stop the default behavior associated with the form submission event. By default, submitting a form leads to a page reload, but calling preventDefault() prevents this default behavior.

5. **Asynchronous Form Submission through AJAX:**

Instead of allowing the default form submission to happen, the provided function (the event handler) uses AJAX (Asynchronous JavaScript and XML) to handle the form submission. AJAX enables sending data to the server and receiving a response without a full page reload. This results in a more seamless and dynamic user experience.

```event.preventDefault();``` Prevents default form submission

```$('#keywordResult').html('<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span><div>');``` This portion of code inserts a loading symbol in the container of ```keywordResult``` to indicate that there is an action taking place
