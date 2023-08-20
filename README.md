# Print Date and Time on Push using GitHub Actions

This repository contains a simple GitHub Actions workflow that runs whenever there's a push to the main branch. The workflow prints the current date and time, providing a demonstration of how to trigger workflows on push events.

## Workflow Details

The workflow is configured to run whenever there's a push to the `main` branch. It uses the `push` event trigger provided by GitHub Actions. When code is pushed to the specified branch, the workflow executes a script that fetches the current date and time and displays it in the workflow logs.

## How to Use

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/Kirag-M-Raj/de_date_time.git
   ```

3. **Customize (Optional):** If you want to modify the branch that triggers the workflow or the behavior of the workflow, you can edit the `.github/workflows/print-date-time.yml` file.

4. **Push Changes:** If you make any changes to the workflow file, commit and push the changes to your repository.

5. **Check Workflow:** Once the changes are pushed to the `main` branch, the workflow will be triggered automatically. Navigate to the "Actions" tab in your GitHub repository to see the workflow runs. You should see runs triggered by pushes to the `main` branch, displaying the current date and time.

## Note

- Be mindful of GitHub Actions usage limits and pricing, especially when running frequent workflow runs triggered by pushes.

## License

This project is licensed under the [MIT License](LICENSE).

