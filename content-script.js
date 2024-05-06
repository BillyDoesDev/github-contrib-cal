console.log(">>> content-script activated <<<");

// (async () => {
//     const response = await fetch("http://127.0.0.1:5000/raccoon");
//     const data = await response.json();
//     console.log(data);
// })();

contribution_calendar = document.querySelector(".ContributionCalendar-grid");
calendar_body = contribution_calendar.querySelector("tbody");
rows = calendar_body.querySelectorAll("tr");
no_rows = rows.length;
no_cols = rows[0].querySelectorAll(".ContributionCalendar-day").length - 1;

console.log(no_rows + " | " + no_cols);

fetch(`http://127.0.0.1:5000/raccoon?apple=${no_rows}-${no_cols}`, {
    method: 'GET'
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
