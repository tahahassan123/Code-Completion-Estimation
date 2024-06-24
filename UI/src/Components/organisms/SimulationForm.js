import React, { useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import LabeledInput from '../molecules/LabeledInput';
import Button from '../atoms/Button';
import axios from 'axios';

// Define validation schema using Yup
const schema = yup.object().shape({
  salary: yup.number().required('Salary is required'),
  productivity: yup.number().required('Productivity is required'),
  min_loc: yup.number().required('Minimum LOC is required'),
  max_loc: yup.number().required('Maximum LOC is required'),
  coding_language: yup.string().required('Coding Language is required'),
  project_type: yup.string().required('Project Type is required'),
  min_fp: yup.number().required('Minimum Functional Points are required'),
  max_fp: yup.number().required('Maximum Functional Points are required'),
  external_inputs: yup.number().required('External Inputs are required'),
  external_outputs: yup.number().required('External Outputs are required'),
  inquiries: yup.number().required('Inquiries are required'),
  external_files: yup.number().required('External Files are required'),
  internal_files: yup.number().required('Internal Files are required'),
  min_test_cases: yup.number().required('Minimum Test Cases are required'),
  max_test_cases: yup.number().required('Maximum Test Cases are required'),
  min_success_rate: yup.number().min(0).max(1).required('Minimum Success Rate is required'),
  max_success_rate: yup.number().min(0).max(1).required('Maximum Success Rate is required'),
  min_internal_cost: yup.number().required('Minimum Internal Cost is required'),
  max_internal_cost: yup.number().required('Maximum Internal Cost is required'),
  min_external_cost: yup.number().nullable(),
  max_external_cost: yup.number().nullable(),
  num_simulations: yup.number().required('Number of Simulations is required'),
  external_resources: yup.boolean().required(),
});

const SimulationForm = ({ runSimulation }) => {
  const { control, handleSubmit, formState: { errors } } = useForm({
    resolver: yupResolver(schema),
    defaultValues: {
      salary: 50000,
      productivity: 100,
      min_loc: 10000,
      max_loc: 20000,
      coding_language: 'python',
      project_type: 'Embedded',
      min_fp: 100,
      max_fp: 200,
      external_inputs: 10,
      external_outputs: 10,
      inquiries: 5,
      external_files: 3,
      internal_files: 5,
      min_test_cases: 500,
      max_test_cases: 1000,
      min_success_rate: 0.8,
      max_success_rate: 0.9,
      min_internal_cost: 100000,
      max_internal_cost: 200000,
      external_resources: true,
      min_external_cost: 20000,
      max_external_cost: 50000,
      num_simulations: 1000
    }
  });

  const [isLoading, setIsLoading] = useState(false);

  const onSubmit = async (data) => {
    console.log("Form Data:", data); // Log the form data
    setIsLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/estimate', data, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      runSimulation(response.data);
    } catch (error) {
      if (error.response) {
        // Server responded with a status other than 200 range
        console.error('Failed to run simulation:', error.response.data);
        alert(`An error occurred: ${error.response.data.detail}`);
      } else if (error.request) {
        // Request was made but no response received
        console.error('Error with request:', error.request);
        alert('No response received. Please check your server.');
      } else {
        // Something else happened
        console.error('Error:', error.message);
        alert('An error occurred. Please try again.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="bg-gray-900 p-6 rounded-lg shadow-md border border-gray-700 space-y-6">
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <LabeledInput label="Salary" name="salary" type="select" control={control} error={errors.salary} options={[
          { value: 50000, label: 'New Programmer ($50,000)' },
          { value: 80000, label: 'Experienced Programmer ($80,000)' },
          { value: 100000, label: 'Professional Programmer ($100,000)' },
        ]} />
        <LabeledInput label="Productivity" name="productivity" type="select" control={control} error={errors.productivity} options={[
          { value: 50, label: 'New Programmer (50 LOC/day)' },
          { value: 80, label: 'Experienced Programmer (80 LOC/day)' },
          { value: 100, label: 'Professional Programmer (100 LOC/day)' },
        ]} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Min LOC" name="min_loc" type="number" control={control} error={errors.min_loc} />
        <LabeledInput label="Max LOC" name="max_loc" type="number" control={control} error={errors.max_loc} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Coding Language" name="coding_language" type="select" control={control} error={errors.coding_language} options={[
          { value: 'python', label: 'Python' },
          { value: 'C++', label: 'C++' },
          { value: 'C', label: 'C' },
          { value: 'Java', label: 'Java' },
          { value: 'C#', label: 'C#' },
          { value: 'JavaScript', label: 'JavaScript' },
        ]} />
        <LabeledInput label="Project Type" name="project_type" type="select" control={control} error={errors.project_type} options={[
          { value: 'Organic', label: 'Organic' },
          { value: 'Semi-detached', label: 'Semi-detached' },
          { value: 'Embedded', label: 'Embedded' },
        ]} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Min Functional Points" name="min_fp" type="number" control={control} error={errors.min_fp} />
        <LabeledInput label="Max Functional Points" name="max_fp" type="number" control={control} error={errors.max_fp} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="External Inputs" name="external_inputs" type="number" control={control} error={errors.external_inputs} />
        <LabeledInput label="External Outputs" name="external_outputs" type="number" control={control} error={errors.external_outputs} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Inquiries" name="inquiries" type="number" control={control} error={errors.inquiries} />
        <LabeledInput label="External Files" name="external_files" type="number" control={control} error={errors.external_files} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Internal Files" name="internal_files" type="number" control={control} error={errors.internal_files} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Min Number of Test Cases" name="min_test_cases" type="number" control={control} error={errors.min_test_cases} />
        <LabeledInput label="Max Number of Test Cases" name="max_test_cases" type="number" control={control} error={errors.max_test_cases} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Min Success Rate" name="min_success_rate" type="number" control={control} error={errors.min_success_rate} />
        <LabeledInput label="Max Success Rate" name="max_success_rate" type="number" control={control} error={errors.max_success_rate} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Min Internal Cost" name="min_internal_cost" type="number" control={control} error={errors.min_internal_cost} />
        <LabeledInput label="Max Internal Cost" name="max_internal_cost" type="number" control={control} error={errors.max_internal_cost} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <LabeledInput label="Min External Cost" name="min_external_cost" type="number" control={control} error={errors.min_external_cost} />
        <LabeledInput label="Max External Cost" name="max_external_cost" type="number" control={control} error={errors.max_external_cost} />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-white mb-2">
          External Resources
          <Controller
            name="external_resources"
            control={control}
            render={({ field }) => (
              <input
                {...field}
                type="checkbox"
                checked={field.value}
                className="ml-2 align-middle"
              />
            )}
          />
        </label>
      </div>

      <LabeledInput label="Number of Simulations" name="num_simulations" type="number" control={control} error={errors.num_simulations} />

      <Button type="submit" className="bg-gradient-to-r from-gray-800 to-gray-700 hover:from-gray-700 hover:to-gray-600 text-white font-bold py-2 px-4 rounded transition duration-300 mt-4">
        {isLoading ? 'Running...' : 'Run Simulation'}
      </Button>
    </form>
  );
};

export default SimulationForm;
