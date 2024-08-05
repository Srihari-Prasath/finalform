// Function to toggle the visibility of the topics section based on the willingness selection
function toggleAdditionalFields() {
    const willingSelect = document.getElementById('willing');
    const topicsSection = document.getElementById('topicsSection');

    if (willingSelect && topicsSection) {
        const selectedValue = willingSelect.value;
        console.log(`Willingness selected: ${selectedValue}`);  // Debug log

        // Toggle visibility based on the selected value
        topicsSection.style.display = selectedValue === 'yes' ? 'block' : 'none';
    } else {
        console.error('Elements for willingness select or topics section not found');
    }
}

// Function to handle topic selection
function handleTopicSelection() {
    const topicCheckboxes = document.querySelectorAll('input[name="topics"]');
    const selectedTopicsContainer = document.getElementById('selectedTopics');

    if (topicCheckboxes.length === 0 || !selectedTopicsContainer) {
        console.error('Topic checkboxes or selected topics container not found');
        return;
    }

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

    // Set up event listener for the willingness select
    const willingSelect = document.getElementById('willing');
    if (willingSelect) {
        willingSelect.addEventListener('change', toggleAdditionalFields);
    } else {
        console.error('Willing select not found');
    }
});
