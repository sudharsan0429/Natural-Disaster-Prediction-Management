<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Natural Disaster Prediction & Management</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f2f5;
            color: #333;
        }
        .header {
            background: linear-gradient(135deg, #2c3e50, #4a6491);
            color: white;
            padding: 25px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .dashboard {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 20px;
            gap: 25px;
        }
        .card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        }
        .card h3 {
            color: #2c3e50;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-top: 0;
        }
        .alert {
            background-color: #e74c3c;
            color: white;
            padding: 12px;
            border-radius: 6px;
            margin: 15px 0;
            font-weight: bold;
        }
        .details-panel {
            display: none;
            background: #f9f9f9;
            border-left: 4px solid #3498db;
            padding: 15px;
            margin-top: 15px;
            border-radius: 0 0 6px 6px;
        }
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #2c3e50;
            color: white;
            margin-top: 30px;
        }
        .severity-low { background-color: #f39c12; }
        .severity-medium { background-color: #e67e22; }
        .severity-high { background-color: #e74c3c; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🌪️ Natural Disaster Prediction & Management</h1>
        <p>Real-time AI-powered monitoring and early warnings</p>
    </div>

    <div class="dashboard">
        <!-- Earthquake Card -->
        <div class="card" onclick="showDetails('earthquake')">
            <h3>🌍 Earthquake Alerts</h3>
            <p>Latest event: <strong>4.2 Magnitude</strong></p>
            <p>Depth: <strong>10.3 km</strong></p>
            <p>Location: <strong>San Andreas Fault, CA</strong></p>
            <div class="alert severity-medium">⚠️ Potential for aftershocks</div>
            <div id="earthquake-details" class="details-panel">
                <h4>Detailed Analysis</h4>
                <p>🔄 Last 7 days activity: 12 tremors</p>
                <p>📈 Trend: Increasing frequency</p>
                <p>🔍 Nearest city: 25km from Los Angeles</p>
                <p>🛡️ Recommended action: Secure heavy furniture</p>
            </div>
        </div>

        <!-- Flood Card -->
        <div class="card" onclick="showDetails('flood')">
            <h3>🌊 Flood Risk Prediction</h3>
            <p>River level: <strong>8.2m (High)</strong></p>
            <p>Rainfall (24h): <strong>65mm</strong></p>
            <p>Soil saturation: <strong>92%</strong></p>
            <div class="alert severity-high">⚠️ Flood warning active</div>
            <div id="flood-details" class="details-panel">
                <h4>Flood Forecast</h4>
                <p>⏳ Expected peak: 14 hours</p>
                <p>📉 Receding in: 36-48 hours</p>
                <p>🚧 Affected roads: Highway 101, Route 66</p>
                <p>🧭 Evacuation centers: 3 active in region</p>
            </div>
        </div>

        <!-- Wildfire Card -->
        <div class="card" onclick="showDetails('wildfire')">
            <h3>🔥 Wildfire Detection</h3>
            <p>Active fires: <strong>8</strong></p>
            <p>Largest fire: <strong>450 acres</strong></p>
            <p>Wind speed: <strong>22 mph (WNW)</strong></p>
            <div class="alert severity-high">🚨 Evacuation in progress</div>
            <div id="wildfire-details" class="details-panel">
                <h4>Fire Spread Analysis</h4>
                <p>📡 Detection method: Satellite + UAVs</p>
                <p>🔥 Current spread rate: 1.2km/h</p>
                <p>🏠 Threatened homes: 142</p>
                <p>🚒 Firefighters deployed: 87</p>
            </div>
        </div>
    </div>

    <div class="footer">
        <p>© 2024 Disaster Intelligence | Data updates every 5 minutes</p>
    </div>

    <script>
        // Track currently open details panel
        let currentOpenPanel = null;

        function showDetails(disasterType) {
            // Hide the currently open panel if exists
            if (currentOpenPanel) {
                currentOpenPanel.style.display = 'none';
            }

            // Show the clicked panel if it's different from current
            const panel = document.getElementById(`${disasterType}-details`);
            if (panel !== currentOpenPanel) {
                panel.style.display = 'block';
                currentOpenPanel = panel;
            } else {
                currentOpenPanel = null;
            }
        }

        // Close panel when clicking anywhere else
        document.addEventListener('click', function(event) {
            if (!event.target.closest('.card') && currentOpenPanel) {
                currentOpenPanel.style.display = 'none';
                currentOpenPanel = null;
            }
        });
    </script>
</body>
</html>