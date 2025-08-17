<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GPA Calculator</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .container {
      background-color: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      text-align: center;
      max-width: 400px;
      width: 100%;
    }

    h1 {
      font-size: 24px;
      margin-bottom: 20px;
    }

    input {
      padding: 10px;
      width: 80%;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    button {
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }

    .result {
      margin-top: 20px;
      font-size: 18px;
      color: #333;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>GPA Calculator</h1>
    <p>Enter your study number to calculate your GPA:</p>
    <input type="number" id="studyNumber" placeholder="Enter your study number" required />
    <button id="calculateBtn">Calculate GPA</button>

    <div id="result" class="result"></div>
  </div>

  <script>
    const gradeToGPA = {
      F: 0,
      D: 0.5,
      DD: 1,
      C: 1.5,
      CC: 2,
      B: 2.5,
      BB: 3,
      A: 3.5,
      AA: 4,
    };

    const sem1 = [
      { name: "Math1", units: 12 },
      { name: "Physics1", units: 12 },
      { name: "English1", units: 9 },
      { name: "Statistics", units: 9 },
      { name: "Arabic", units: 6 },
      { name: "Computer", units: 9 },
    ];

    const sem2 = [
      { name: "Math2", units: 12 },
      { name: "Physics2", units: 12 },
      { name: "Chemistry", units: 9 },
      { name: "Drawing", units: 6 },
      { name: "English2", units: 9 },
    ];

    const pastebinLinks = {
      Math1_old: "https://pastebin.com/raw/4WscJMh0",
      Math1_new: "https://pastebin.com/raw/xBmPwP5u",
      Physics1_old: "https://pastebin.com/raw/VsZXLGnF",
      Physics1_new: "https://pastebin.com/raw/XZeQHFSs",
      English1_old: "https://pastebin.com/raw/AxmBtNeE",
      English1_new: "https://pastebin.com/raw/ZZsjVX30",
      Statistics_old: "https://pastebin.com/raw/DY08wqAx",
      Statistics_new: "https://pastebin.com/raw/2WeYNGM2",
      Arabic_old: "https://pastebin.com/raw/pUdtTdDC",
      Arabic_new: "https://pastebin.com/raw/S5R0pKKn",
      Computer_old: "https://pastebin.com/raw/xM78SjCp",
      Computer_new: "https://pastebin.com/raw/8fZNVW1s",
      Math2: "https://pastebin.com/raw/eSiuC5ML",
      Physics2: "https://pastebin.com/raw/e3FQwB9q",
      Chemistry: "https://pastebin.com/raw/izG7PzL5",
      Drawing: "https://pastebin.com/raw/QGnc3Duj",
      English2: "https://pastebin.com/raw/yBdzjstv",
    };

    async function fetchGradeFromPastebin(url) {
      try {
        const response = await fetch(url);
        return response.text();
      } catch (error) {
        console.error("Error fetching from Pastebin:", error);
        return null;
      }
    }

    function calculateSubjectGPA(subject, grade) {
      const gpa = gradeToGPA[grade];
      return gpa * subject.units;
    }

    async function calculateGPA(studyNumber) {
      let totalUnits = 0;
      let totalGPA = 0;

      for (const subject of sem1) {
        const gradeOld = await fetchGradeFromPastebin(pastebinLinks[`${subject.name}_old`]);
        const gradeNew = await fetchGradeFromPastebin(pastebinLinks[`${subject.name}_new`]);

        let grade = gradeOld;
        if (gradeNew && gradeNew !== 'F') {
          grade = gradeNew;
        }

        const subjectGPA = calculateSubjectGPA(subject, grade);
        totalUnits += subject.units;
        totalGPA += subjectGPA;
      }

      for (const subject of sem2) {
        const grade = await fetchGradeFromPastebin(pastebinLinks[subject.name]);
        const subjectGPA = calculateSubjectGPA(subject, grade);
        totalUnits += subject.units;
        totalGPA += subjectGPA;
      }

      const finalGPA = totalGPA / totalUnits;
      return finalGPA.toFixed(2);
    }

    document.getElementById("calculateBtn").addEventListener("click", async () => {
      const studyNumber = document.getElementById("studyNumber").value;
      if (!studyNumber) {
        alert("Please enter your study number.");
        return;
      }

      document.getElementById("result").innerHTML = "Calculating GPA...";

      const gpa = await calculateGPA(studyNumber);
      document.getElementById("result").innerHTML = `Your GPA is: ${gpa}`;
    });
  </script>
</body>
</html>
