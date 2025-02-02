import React from 'react';

const ComplaintList = ({complaints}) => {
    return (
        <div>
            <div className="mt-6 flow-root sm:mt-8">
                <div className="divide-y divide-gray-200 dark:divide-gray-700">
                { complaints ? (complaints.map((complaint) => (
                    <div
                        key={complaint.complaintId}
                        className="relative bg-gray-50 p-5 rounded shadow grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5"
                    >
                        {/* Complaint Name */}
                        <div className="col-span-1 flex items-center sm:col-span-4 lg:col-span-1">
                            <span className="text-base font-semibold text-gray-900 hover:underline dark:text-white">
                                {complaint.sourceId || "Author"}
                            </span>
                        </div>                        

                        {/* Complaint Date */}
                        <div className="flex col-span-1 items-center justify-center">
                            <p className="text-sm text-gray-500 dark:text-gray-400">
                                <span className="font-medium text-gray-900 dark:text-white">
                                    Date
                                </span>
                                : {complaint.date || "Unknown date"}
                            </p>
                        </div>

                        <div className="flex col-span-3 items-center justify-center">
                            <p className="text-sm text-gray-500 dark:text-gray-400">
                                <span className="font-medium text-gray-900 dark:text-white">Message
                                </span>
                                : {complaint.content || "No Content"}
                            </p>
                        </div>
                    </div>

                    )) ) : (
                        <p>No complaints</p>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ComplaintList;