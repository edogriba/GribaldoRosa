import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { StudentTab } from './StudentTab';
import StudentProfileCard from './StudentProfileCard';
import StudentProfileTable from './StudentProfileTable';
import { UserContext } from '../../../context/UserContext';

const StudentProfile = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
            <div>
                <Navbar user={user} onLogout={userLogout}/>
                <StudentTab activeTab='profile'/>
            </div>
                <div className='flex p-5 justify-evenly'>
                    <StudentProfileCard />
                    <StudentProfileTable />
                </div>
            <Footer />
        </div>
    );
};

export default StudentProfile;