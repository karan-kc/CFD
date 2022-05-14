/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Copyright (C) YEAR OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/

#include "functionObjectTemplate.H"
#include "fvCFD.H"
#include "unitConversion.H"
#include "addToRunTimeSelectionTable.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

defineTypeNameAndDebug(calcGradUFunctionObject, 0);

addRemovableToRunTimeSelectionTable
(
    functionObject,
    calcGradUFunctionObject,
    dictionary
);


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C"
{
    // dynamicCode:
    // SHA1 = f0d97ebb7ad3dce54b3e67499a59844095d42ae8
    //
    // unique function name that can be checked if the correct library version
    // has been loaded
    void calcGradU_f0d97ebb7ad3dce54b3e67499a59844095d42ae8(bool load)
    {
        if (load)
        {
            // code that can be explicitly executed after loading
        }
        else
        {
            // code that can be explicitly executed before unloading
        }
    }
}


// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * Private Member Functions  * * * * * * * * * * * //

const fvMesh& calcGradUFunctionObject::mesh() const
{
    return refCast<const fvMesh>(obr_);
}


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

calcGradUFunctionObject::calcGradUFunctionObject
(
    const word& name,
    const Time& runTime,
    const dictionary& dict
)
:
    functionObjects::regionFunctionObject(name, runTime, dict)
{
    read(dict);
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

calcGradUFunctionObject::~calcGradUFunctionObject()
{}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

bool calcGradUFunctionObject::read(const dictionary& dict)
{
    if (false)
    {
        Info<<"read calcGradU sha1: f0d97ebb7ad3dce54b3e67499a59844095d42ae8\n";
    }

//{{{ begin code
    #line 62 "/home/ensm_student/Documents/CFD/Rechnerubung/Week2/Aufgabe1/RANS/system/controlDict.functions.calcGradU"
const volVectorField& U = mesh().lookupObjectRef<volVectorField>("U");

      autoPtr<volTensorField> gradU;
      gradU.reset
      (
        new volTensorField 
        (
          IOobject
          (
              "gradU",
              mesh().time().timeName(),
              mesh(),
              IOobject::NO_READ,
              IOobject::AUTO_WRITE
          ),
          fvc::grad(U)
        )
      );
      gradU->store(gradU);
//}}} end code

    return true;
}


bool calcGradUFunctionObject::execute()
{
    if (false)
    {
        Info<<"execute calcGradU sha1: f0d97ebb7ad3dce54b3e67499a59844095d42ae8\n";
    }

//{{{ begin code
    #line 85 "/home/ensm_student/Documents/CFD/Rechnerubung/Week2/Aufgabe1/RANS/system/controlDict.functions.calcGradU"
const volVectorField& U = mesh().lookupObjectRef<volVectorField>("U");
        volTensorField& gradU = mesh().lookupObjectRef<volTensorField>("gradU");

        Info << "Calculating grad(U)." << endl;
        gradU = fvc::grad(U);

        if(mesh().time().outputTime()){ gradU.write(); }
//}}} end code

    return true;
}


bool calcGradUFunctionObject::write()
{
    if (false)
    {
        Info<<"write calcGradU sha1: f0d97ebb7ad3dce54b3e67499a59844095d42ae8\n";
    }

//{{{ begin code
    
//}}} end code

    return true;
}


bool calcGradUFunctionObject::end()
{
    if (false)
    {
        Info<<"end calcGradU sha1: f0d97ebb7ad3dce54b3e67499a59844095d42ae8\n";
    }

//{{{ begin code
    
//}}} end code

    return true;
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

