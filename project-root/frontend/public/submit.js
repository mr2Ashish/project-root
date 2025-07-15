document.getElementById('dataForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = {
    name: e.target.name.value,
    email: e.target.email.value
  };

  try {
    const response = await fetch('http://localhost:5000/api/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });

    const data = await response.json();
    alert('Response: ' + JSON.stringify(data));
  } catch (err) {
    console.error('Error:', err);
  }
});
