$(document).ready(function() {
    // Function to toggle input field based on selected option
    function toggleInputField() {
        // Get the selected value from the dropdown
        var inputType = $('#inputType').val();

        // Modify input field based on the selected option
        if (inputType === 'url') {
            // If 'url' is selected, set input type to 'url', adjust placeholder and styling
            $('#inputValue').attr('placeholder', 'Enter URL').attr('type', 'url').css('height', '100px');
            $('#inputLabel').text('Enter URL:');
        } else if (inputType === 'description') {
            // If 'description' is selected, set input type to 'text', adjust placeholder and styling
            $('#inputValue').attr('placeholder', 'Enter Product Description').attr('type', 'text').css('height', '200px');
            $('#inputLabel').text('Enter Product Description:');
        }

        // Reset text field
        $('#inputValue').val('');
    }

    // Toggle input field on page load
    toggleInputField();

    // Toggle input field when dropdown value changes
    $('#inputType').change(function() {
        toggleInputField();
    });

    $('#keywordForm').submit(function(event) {
        // Prevent default form submission
        event.preventDefault();

        // Show loading spinner
        $('#keywordResult').html('<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>');

        // Get the input value
        var inputValue = $('#inputValue').val();

        // Make AJAX request to the server
        $.ajax({
            type: 'POST',
            url: '/generate_keywords',
            data: {inputType: $('#inputType').val(), inputValue: inputValue},
            success: function(data) {
                // Clear previous results
                $('#keywordResult').empty();

                // Create an unordered list
                var keywordList = $('<ul>').addClass('list-group');
                var listItem = $('<li>').addClass('list-group-item').text('Generated Keywords');
                listItem.addClass('bg-custom text-white');
                keywordList.append(listItem);

                // Add list items for each keyword
                data.keywords.forEach(function(keyword) {
                    var listItem = $('<li>').addClass('list-group-item').text(keyword);
                    keywordList.append(listItem);
                });

                // Append the list to the result div
                $('#keywordResult').append(keywordList);
            },
            error: function() {
                alert('An error occurred while generating keywords.');
            }
        });

        // This prevents the default form submission behavior
        return false;
    });
});
