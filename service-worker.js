// chrome.runtime.onInstalled.addListener(() => {
//     chrome.action.setBadgeText({
//         text: "OFF",
//     });
// });


chrome.action.onClicked.addListener(async (tab) => {

    // if (tab.url.includes("")) {
    //     // Retrieve the action badge to check if the extension is 'ON' or 'OFF'
    //     const prevState = await chrome.action.getBadgeText({ tabId: tab.id });
    //     // Next state will always be the opposite
    //     const nextState = prevState === 'ON' ? 'OFF' : 'ON';

    //     location.reload();

    //     // Set the action badge to the next state
    //     await chrome.action.setBadgeText({
    //         tabId: tab.id,
    //         text: nextState,
    //     });
    // }


    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content-script.js"]
    });
});