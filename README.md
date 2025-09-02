PhonePe Analytics Dashboard
A comprehensive analytics dashboard for visualizing user data, transaction trends, and geographical distribution across India for the PhonePe digital payments platform.

Features
Summary Cards: Key metrics including total users, popular banks, states, and transaction volume

Interactive Charts: Visualizations for bank usage, state-wise distribution, email domains, and demographics

Transaction Analytics: Trends and state-wise transaction volume analysis

India Map Visualization: Interactive map showing user distribution across Indian states

Responsive Design: Works seamlessly on desktop and mobile devices

Technologies Used
HTML5, CSS3, JavaScript (ES6+)

Chart.js for data visualizations

Font Awesome for icons

Google Fonts (Inter) for typography

SVG for India map visualization

Data Sources
The dashboard uses multiple data sources:

API endpoints for real-time data (when available)

Mock data generation for demonstration purposes

State-wise user distribution data for map visualization

API Endpoints
The dashboard attempts to fetch data from these endpoints:

/api/summary - Overall statistics

/api/popular-banks - Bank usage data

/api/popular-states - State distribution

/api/email-domains - Email provider statistics

/api/user-demographics - Age and gender data

/api/transaction-trends - Transaction history

/api/state-wise-data - State-specific metrics

Installation
Clone the repository:

bash
git clone <repository-url>
Navigate to the project directory:

bash
cd phonepe-analytics-dashboard
Open index.html in a web browser:

bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve
Access the dashboard at http://localhost:8000

Usage
View Summary Metrics: Check the summary cards at the top for key statistics

Explore Charts: Interact with various charts to understand user behavior patterns

Analyze Demographics: Use the tabs in the demographics chart to switch between age groups and gender data

Hover over Map: Explore state-wise distribution by hovering over the India map

Download Data: Use the download button on any chart to export the data

Customization
Adding New Charts
Add HTML structure in the charts-grid section

Create a canvas element with a unique ID

Add corresponding JavaScript code to fetch data and render the chart

Modifying Color Scheme
Update the CSS custom properties in the :root selector:

css
:root {
  --primary: #your-color;
  --secondary: #your-color;
  /* ... other colors */
}
Adding API Endpoints
Modify the fetchData() function calls in the initializeDashboard() function to point to your API endpoints.

Data Structure
Mock Data Generation
The dashboard includes functions to generate realistic mock data:

generateMockDemographics() - Age groups and gender distribution

generateMockTransactionTrends() - Monthly transaction data

generateMockStateTransactions() - State-wise transaction volume

generateMockStateUserData() - State-wise user distribution for the map

Expected API Responses
javascript
// Summary endpoint
{
  "total_users": 12458,
  "popular_bank": "State Bank of India",
  "popular_state": "Maharashtra",
  "transaction_volume": 1427500000
}

// Popular banks endpoint
{
  "State Bank of India": 2450,
  "HDFC Bank": 1980,
  // ... other banks
}
Browser Compatibility
Chrome (recommended)

Firefox

Safari

Edge

Performance Notes
Charts are rendered client-side using Chart.js

The India map uses optimized SVG paths for performance

Mock data is generated on-demand to reduce initial load time

Contributing
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
PhonePe for inspiration

Chart.js for powerful charting capabilities

Contributors and testers

Support
For support or questions about this dashboard, please create an issue in the repository or contact the development team.

Version History
1.0.0

Initial release with core functionality

Interactive charts and India map visualization

Mock data generation for demonstration

