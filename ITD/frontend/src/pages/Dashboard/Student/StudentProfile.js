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
        <div>
            <Navbar isLoggedIn={!!user} onLogout={userLogout}/>
            <StudentTab activeTab='profile'/>
                <div className='flex bg-gray-50'>
                    <StudentProfileCard />
                    <StudentProfileTable />
                </div>
            <Footer />
        </div>
    );
};

export default StudentProfile;