const gradeToGPA = {
    'F': 0, 'D': 0.5, 'DD': 1, 'C': 1.5, 'CC': 2,
    'B': 2.5, 'BB': 3, 'A': 3.5, 'AA': 4
};

const sem1 = [
    { name: "Math1", units: 12 },
    { name: "Physics1", units: 12 },
    { name: "English1", units: 9 },
    { name: "Statistics", units: 9 },
    { name: "Arabic", units: 6 },
    { name: "Computer", units: 9 }
];

const sem2 = [
    { name: "Math2", units: 12 },
    { name: "Physics2", units: 12 },
    { name: "Chemistry", units: 9 },
    { name: "Drawing", units: 6 },
    { name: "English2", units: 9 }
];

const pastebinLinks = {
    'Math1_old': 'https://pastebin.com/raw/4WscJMh0',
    'Math1_new': 'https://pastebin.com/raw/1NcsJK7g',
    'Physics1_old': 'https://pastebin.com/raw/VsZXLGnF',
    'Physics1_new': 'https://pastebin.com/raw/XZeQHFSs',
    'English1_old': 'https://pastebin.com/raw/AxmBtNeE',
    'English1_new': 'https://pastebin.com/raw/ZZsjVX30',
    'Statistics_old': 'https://pastebin.com/raw/DY08wqAx',
    'Statistics_new': 'https://pastebin.com/raw/2WeYNGM2',
    'Arabic_old': 'https://pastebin.com/raw/pUdtTdDC',
    'Arabic_new': 'https://pastebin.com/raw/S5R0pKKn',
    'Computer_old': 'https://pastebin.com/raw/xM78SjCp',
    'Computer_new': 'https://pastebin.com/raw/8fZNVW1s',
    'Math2': 'https://pastebin.com/raw/eSiuC5ML',
    'Physics2': 'https://pastebin.com/raw/e3FQwB9q',
    'Chemistry': 'https://pastebin.com/raw/izG7PzL5',
    'Drawing': 'https://pastebin.com/raw/QGnc3Duj',
    'English2': 'https://pastebin.com/raw/yBdzjstv'
};

async function fetchGradeData(url) {
    try {
        // Try multiple CORS proxy services
        const proxies = [
            'https://api.allorigins.win/raw?url=',
            'https://corsproxy.io/?',
            'https://cors-anywhere.herokuapp.com/',
            '' // Direct fetch as fallback
        ];
        
        let response, text;
        let lastError;
        
        for (const proxy of proxies) {
            try {
                const proxyUrl = proxy + encodeURIComponent(url);
                console.log(`Trying to fetch from: ${proxyUrl}`);
                
                response = await fetch(proxyUrl);
                if (response.ok) {
                    text = await response.text();
                    console.log(`Success with proxy: ${proxy}`);
                    break;
                }
            } catch (error) {
                console.log(`Failed with proxy ${proxy}:`, error.message);
                lastError = error;
                continue;
            }
        }
        
        if (!text) {
            throw lastError || new Error('All proxy attempts failed');
        }
        
        const grades = {};
        
        // Debug: Log the raw text
        console.log(`Data from ${url}:`, text.substring(0, 200) + '...');
        
        const lines = text.split('\n');
        lines.forEach((line, index) => {
            const trimmed = line.trim();
            if (trimmed && trimmed.includes(':')) {
                const parts = trimmed.split(':');
                if (parts.length >= 2) {
                    const studentNum = parts[0].trim();
                    const grade = parts[1].trim();
                    if (studentNum && grade) {
                        grades[studentNum] = grade;
                    }
                }
            } else if (trimmed && /^\d+\s+[A-Z]+$/.test(trimmed)) {
                // Handle format like "33039 AA" (space separated)
                const parts = trimmed.split(/\s+/);
                if (parts.length >= 2) {
                    const studentNum = parts[0].trim();
                    const grade = parts[1].trim();
                    if (studentNum && grade) {
                        grades[studentNum] = grade;
                    }
                }
            }
        });
        
        // Debug: Log found grades
        console.log(`Grades found in ${url}:`, Object.keys(grades).length, 'students');
        
        return { grades, rawText: text, url };
    } catch (error) {
        console.error('Error fetching data from:', url, error);
        return { grades: {}, rawText: '', url, error: error.message };
    }
}

// Add remaining functions for GPA calculation, displaying results, and other functionality.
