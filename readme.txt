# AI Assistant for Transportation Decision

This script simulates an AI assistant that recommends transportation modes 
(work from home, take public transport, or drive) 
based on various conditions 
(rain, traffic, construction, etc.). 
It also suggests specific routes if driving is the recommended option.

## Variables:
- `rain`
- `heavyTraffic`
- `construction`
- `earlyMeeting`
- `strike`
- `doctorAppointment`

## Transportation Options:
- **Work from Home (WFH)**: Suggested if certain conditions (rain, early meeting, strike, etc.) are met.
- **Public Transport**: Recommended if there's no strike and WFH isn't suggested.
- **Drive**: Recommended if neither WFH nor public transport is suitable.

### Routes when Driving:
- **Road 1**: No construction or heavy traffic.
- **Road 2**: Heavy traffic but no construction.
- **Road 3**: Construction but no heavy traffic.
- **Road 4**: Both construction and heavy traffic.

## Usage:
The `ai_assistant()` function takes a `scenario` (logical conditions) and prints the best transportation recommendation.

### Example Scenarios:
1. **Scenario 1**: Rain and heavy traffic.
2. **Scenario 2**: Strike.
3. **Scenario 3**: All false.