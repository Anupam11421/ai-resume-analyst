document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('resumeForm');
  const spinner = document.getElementById('spinner');
  const analyzeBtn = form.querySelector('button[type="submit"]');
  const fileInput = form.querySelector('input[type="file"]');

  // Initially disable the button
  analyzeBtn.disabled = true;

  // Enable button only when a file is selected
  fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    if (file && file.type === "application/pdf") {
      analyzeBtn.disabled = false;
    } else {
      analyzeBtn.disabled = true;
      alert("Please upload a valid PDF resume.");
    }
  });

  // Show spinner and change button text on submit
  form.addEventListener('submit', () => {
    spinner.classList.remove('hidden');
    analyzeBtn.textContent = 'Analyzing... 🔍';
    analyzeBtn.disabled = true;
  });
});
