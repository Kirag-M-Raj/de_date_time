

# Print Date and Time using GitHub Actions

This repository contains a simple GitHub Actions workflow that runs on a schedule to print the current date and time. It serves as a demonstration of how to set up scheduled workflows in GitHub Actions.

## Workflow Details

The workflow is configured to run every 10 minutes using the `schedule` event provided by GitHub Actions. It runs a script that fetches the current date and time and displays it in the workflow logs.

## How to Use

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/Kirag-M-Raj/de_date_time.git
   ```

2. **Customize (Optional):** If you want to modify the schedule or the behavior of the workflow, you can edit the `.github/workflows/print-date-time.yml` file.

3. **Push Changes:** If you make any changes to the workflow file, commit and push the changes to your repository.

4. **Check Workflow:** Once the changes are pushed, navigate to the "Actions" tab in your GitHub repository to see the workflow runs. You should see runs every 10 minutes displaying the current date and time.

## Note

- Be mindful of GitHub Actions usage limits and pricing, especially when running scheduled workflows frequently.

## License

This project is licensed under the [MIT License](LICENSE).

---
