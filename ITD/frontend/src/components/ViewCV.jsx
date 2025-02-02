import React from 'react';

const downloadPDF = () => {
    const link = document.createElement("a");
    link.href = "http://localhost:5000/download-pdf";
    link.download = "CV.pdf"; // Suggested file name
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};

const ViewCV = () => {
    return (
        <div>
            <button onClick={downloadPDF}>Download PDF</button>
        </div>
    );
};

export default ViewCV;