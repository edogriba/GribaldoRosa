import React from "react";


const Status = ({ status }) => {
        let statusColor;
        switch(status) {
            case 'Rejected':
                statusColor = 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300';
                break;
            case 'Pending':
                statusColor = 'bg-gray-200 text-gray-800 dark:bg-gray-900 dark:text-gray-300';
                break;
            case 'Accepted':
                statusColor = 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300';
                break;
            case 'Confirmed':
                statusColor = 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300';
                break;
            case 'Assessment':
                statusColor = 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300';
                break;
            case 'Refused':
                statusColor = 'bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-300';
                break;
            default:
                statusColor = 'bg-gray-200 text-gray-800 dark:bg-gray-900 dark:text-gray-300';
        }
        return (
            <span className={`inline-flex items-center rounded px-2.5 py-0.5 text-xs font-medium ${statusColor}`}>
                {status || "Unknown"}
            </span>
        );


}

export default Status;