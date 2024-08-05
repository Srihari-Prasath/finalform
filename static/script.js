// Function to toggle the visibility of additional fields based on the willingness checkbox
function toggleAdditionalFields() {
    const willingCheckbox = document.getElementById('willing');
    const additionalFields = document.getElementById('additionalFields');
    additionalFields.style.display = willingCheckbox.checked ? 'block' : 'none';
}

// Function to handle topic selection
function handleTopicSelection() {
    const topicCheckboxes = document.querySelectorAll('input[name="topics"]');
    const selectedTopicsContainer = document.getElementById('selectedTopics');
    
    // Clear previously selected topics
    selectedTopicsContainer.innerHTML = '';
    
    topicCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                const selectedTopic = document.createElement('div');
                selectedTopic.textContent = this.value;
                selectedTopicsContainer.appendChild(selectedTopic);
            } else {
                const selectedTopics = Array.from(selectedTopicsContainer.childNodes);
                selectedTopics.forEach(topic => {
                    if (topic.textContent === this.value) {
                        selectedTopicsContainer.removeChild(topic);
                    }
                });
            }
        });
    });
}

// Initialize event listeners when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the topic selection functionality
    handleTopicSelection();
    
    // Set up event listener for the willing checkbox
    const willingCheckbox = document.getElementById('willing');
    willingCheckbox.addEventListener('change', toggleAdditionalFields);
});
