// This file contains JavaScript code for rendering charts using Chart.js

document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('employeeChart').getContext('2d');
    const employeeChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [], // Populate with employee names or departments
            datasets: [{
                label: 'Employee Performance',
                data: [], // Populate with performance data
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Fetch employee data and update the chart
    fetch('/api/employees/')
        .then(response => response.json())
        .then(data => {
            const labels = data.map(employee => employee.name);
            const performanceData = data.map(employee => employee.performanceScore);
            employeeChart.data.labels = labels;
            employeeChart.data.datasets[0].data = performanceData;
            employeeChart.update();
        })
        .catch(error => console.error('Error fetching employee data:', error));
});