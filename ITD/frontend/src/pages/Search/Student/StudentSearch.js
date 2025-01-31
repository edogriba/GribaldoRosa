import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import SearchFilter from './SearchFilter';
import { UserContext } from '../../../context/UserContext';
import GoBack from '../../../components/GoBack';
import { useNavigate } from 'react-router-dom';

const StudentSearch = () => {  
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
                <Navbar  user={user} onLogout={userLogout}/>
                <div>
                    <GoBack location="students/home"/>
                </div>
                <SearchFilter />
            </div>
            <Footer />
        </div>

    );
};

export default StudentSearch;