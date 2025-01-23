import React from "react"

export const SocialProof = () => {
  return (
    <section className="bg-white dark:bg-gray-900">
      <div className="max-w-screen-xl px-4 py-8 mx-auto text-center lg:py-16 lg:px-6">
        <h2 className="mb-8 lg:mb-16 text-3xl font-extrabold tracking-tight leading-tight text-center text-gray-900 dark:text-white md:text-4xl">S&C in numbers:</h2>
        <dl className="grid max-w-screen-md gap-8 mx-auto text-gray-900 sm:grid-cols-3 dark:text-white">
          <div className="flex flex-col items-center justify-center">
            <dt className="mb-2 text-3xl md:text-4xl font-extrabold">2k+</dt>
            <dd className="font-light text-gray-500 dark:text-gray-400">Companies</dd>
          </div>
          <div className="flex flex-col items-center justify-center">
            <dt className="mb-2 text-3xl md:text-4xl font-extrabold">10k+</dt>
            <dd className="font-light text-gray-500 dark:text-gray-400">Students</dd>
          </div>
          <div className="flex flex-col items-center justify-center">
            <dt className="mb-2 text-3xl md:text-4xl font-extrabold">1k+</dt>
            <dd className="font-light text-gray-500 dark:text-gray-400">Internships</dd>
          </div>
        </dl>
      </div>
    </section>
  )
}

export default SocialProof;