import React from "react"

export const Footer = () => {
    return (
        <footer className="static w-full bg-gray-100 rounded-lg shadow-sm dark:bg-gray-800">
            <div className="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
                <span className="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2025,<a href="" className="hover:underline"> S&C™</a>. All Rights Reserved.
                </span>
                <ul className="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
                    <li>
                        <a href="/" className="hover:underline me-4 md:me-6">Welcome</a>
                    </li>
                    <li>
                        <a href="/about" className="hover:underline me-4 md:me-6">About</a>
                    </li>
                </ul>
            </div>
        </footer>
    )
}

export default Footer;