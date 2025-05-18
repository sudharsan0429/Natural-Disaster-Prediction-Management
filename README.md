# 🌪️ Natural Disaster Prediction & Management

This project is a **responsive web-based dashboard** that provides real-time alerts and detailed insights into various natural disasters like earthquakes, floods, and wildfires. It is designed for clear visualization, interactive data presentation, and user-friendly analysis of disaster risks.

---

## 🚀 Features

- 🌍 **Earthquake Alerts**
  - Displays the latest seismic event with magnitude, depth, and location.
  - Includes historical trends and safety recommendations.

- 🌊 **Flood Risk Prediction**
  - Real-time river level, rainfall stats, and soil saturation metrics.
  - Predictive warnings with evacuation info and infrastructure risks.

- 🔥 **Wildfire Detection**
  - Current fire counts, spread rate, and satellite/UAV-based detection.
  - Evacuation status and firefighting deployment details.

- ⚠️ **Severity Indicators**
  - Color-coded alerts: `Low`, `Medium`, `High`.

- 📊 **Interactive UI**
  - Click-to-expand detail panels.
  - Collapses automatically when clicking outside a card.

---

## 🖼️ UI Overview

- **Header**: Gradient-based title with a subtitle.
- **Dashboard**: Flexbox layout containing cards for each disaster type.
- **Cards**:
  - Summary data.
  - Severity alert banner.
  - Hidden panel with expanded analysis (toggle on click).
- **Footer**: Data update notice.

---

## 📁 Project Structure

All content is in a single `index.html` file:

- **HTML**: Semantic structure with disaster cards.
- **CSS**: Responsive layout, cards with hover effects, alerts, and visual enhancements.
- **JavaScript**:
  - Expands/collapses individual disaster details.
  - Ensures only one panel is open at a time.
  - Closes panels when clicking outside.

---

## 💡 How It Works

1. **Click a card**: Shows disaster-specific insights in a details panel.
2. **Click another card**: Closes the previous and opens the new one.
3. **Click outside**: All detail panels close.

---

## 📱 Responsive Design

The layout uses Flexbox and adapts well to medium and large screens. For smaller devices, consider adding media queries to improve card width responsiveness.

```css
@media (max-width: 600px) {
    .card {
        width: 90%;
    }
}
# Natural-Disaster-Prediction-Management
