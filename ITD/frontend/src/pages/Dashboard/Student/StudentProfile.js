import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { StudentTab } from './StudentTab';
import StudentProfileCard from './StudentProfileCard';
import StudentProfileTable from './StudentProfileTable';
import { UserContext } from '../../../context/UserContext';
import { useNavigate } from 'react-router-dom';

const StudentProfile = () => {
    const { user, userLogout } = useContext(UserContext);
    const navigate = useNavigate();
    useEffect(() => {
        if(user.type !== 'student') {
            navigate('/login');
        }
    }, [user]);
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