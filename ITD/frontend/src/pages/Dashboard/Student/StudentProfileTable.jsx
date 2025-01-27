import React, {useContext} from 'react';
import { UserContext } from '../../../context/UserContext';

const StudentProfileTable = ({ students }) => {
    const { user } = useContext(UserContext);
    
    return (
        <section className=" dark:bg-gray-900 p-3 sm:p-5">
            <div className="mx-auto max-w-screen-xl px-4 lg:px-12">
                <div className="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
                    <div className="overflow-x-auto">
                        {/* Table 1 */}
                        <table className="w-full border-t text-sm text-left text-gray-500 dark:text-gray-400 table-fixed">
                            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th className="w-1/4 px-4 py-3">Name</th>
                                    <th className="w-1/4 px-4 py-3">Surname</th>
                                    <th className="w-1/4 px-4 py-3">Phone Number</th>
                                    <th className="w-1/4 px-4 py-3">Location</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr className="border-t dark:border-gray-700">
                                    <td className="px-4 py-3">{user.firstName}</td>
                                    <td className="px-4 py-3">{user.lastName}</td>
                                    <td className="px-4 py-3">{user.phoneNumber}</td>
                                    <td className="px-4 py-3">{user.location}</td>
                                </tr>
                            </tbody>
                        </table>

                        {/* Table 2 */}
                        <table className="w-full border-t text-sm text-left text-gray-500 dark:text-gray-400 table-fixed mt-5">
                            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th className="w-1/4 px-4 py-3">Degree Program</th>
                                    <th className="w-1/4 px-4 py-3">GPA</th>
                                    <th className="w-1/4 px-4 py-3">Graduation Date</th>
                                    <th className="w-1/4 px-4 py-3">University ID</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr className="border dark:border-gray-700">
                                    <td className="px-4 py-3">{user.degreeProgram}</td>
                                    <td className="px-4 py-3">{user.GPA}</td>
                                    <td className="px-4 py-3">{user.graduationYear}</td>
                                    <td className="px-4 py-3">{user.universityId}</td>
                                </tr>
                            </tbody>
                        </table>

                        {/* Table 3 */}
                        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400 table-fixed mt-5">
                            <tbody>
                                <tr className="border-b dark:border-gray-700">
                                    <th className="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white w-1/4">Skills</th>
                                    <td className="px-4 py-3 w-3/4">{user.skills}</td>
                                </tr>
                            </tbody>
                        </table>

                        {/* Table 4 */}
                        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400 table-fixed mt-5">
                            <tbody>
                                <tr className="border-b dark:border-gray-700">
                                    <th className="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white w-1/4">Languages Spoken</th>
                                    <td className="px-4 py-3 w-3/4">{user.languageSpoken}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default StudentProfileTable;