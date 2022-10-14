# Copyright (C) 2022 DJ_Level_3
# This file is part of PyRiff <https://github.com/DJLevel3/PyRiff>.
#
# PyRiff is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyRiff is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyRiff.  If not, see <http://www.gnu.org/licenses/>.

import struct

class Chunk:
    def __init__(self, ckID):
        self.id = _checkFourChar(ckID)
    
    def dataToBin(self):
        return bytearray("datagoeshere".encode())

    def getBinary(self):
        dataBinary = self.dataToBin()
        finalBinary = bytearray()
        finalBinary.extend(self.id.encode())
        finalBinary.extend(len(dataBinary).to_bytes(4, 'little'))
        finalBinary.extend(dataBinary)
        return finalBinary

class ChunkBin(Chunk):
    def __init__(self, ckID):
        super().__init__(ckID)
        self.dataBin = bytearray()
    
    def dataToBin(self):
        return self.dataBin
    
    def set(self, newData):
        if (type(newData) != bytearray):
            raise TypeError("Must provide data in bytearray form!")
        else:
            self.dataBin = newData
    
    def get(self, start=0, end=-1):
        if end == -1:
            end = self.dataBin.size()
        return self.dataBin[start:end]
    
    def extend(self, newData):
        if (type(newData) != bytearray):
            raise TypeError("Must provide data in bytearray form!")
        else:
            self.dataBin.extend(newData)

class ChunkStr(ChunkBin):
    def __init__(self, ckID):
        super().__init__(ckID)

    def set(self, newData):
        if (type(newData) != str):
            raise TypeError("Must provide data in str form!")
        self.dataBin = bytearray(newData.encode())
    
    def extend(self, newData):
        if (type(newData) != str):
            raise TypeError("Must provide data in str form!")
        self.dataBin.extend(bytearray(newData.encode()))
    
    def get(self, start=0, end=0):
        if end == 0:
            end = self.dataBin.size()
        return str(self.dataBin[start:end],'utf-8')

class ChunkInt32(Chunk):
    def __init__(self, ckID):
        super().__init__(ckID)
        self.dataList = []
    
    def dataToBin(self):
        if len(self.dataList) == 0:
            raise ValueError("Int32 chunk must contain at least one value!")
        else:
            dataBinary = bytearray()
            for i in self.dataList:
                dataBinary.extend(struct.pack("<i", i))
            return dataBinary
    
    def set(self, newData):
        if (type(newData) != int):
            raise TypeError("Must provide data in int form!")
        else:
            self.dataList = [newData]
    
    def append(self, newData):
        if (type(newData) != int):
            raise TypeError("Must provide data in int form!")
        else:
            self.dataList.append(newData)
    
    def get(self, index):
        return self.dataList[index]

class ChunkInt16(Chunk):
    def __init__(self, ckID):
        super().__init__(ckID)
        self.dataList = []
    
    def dataToBin(self):
        if len(self.dataList) == 0:
            raise ValueError("Int16 chunk must contain at least one value!")
        else:
            dataBinary = bytearray()
            for i in self.dataList:
                dataBinary.extend(struct.pack("<h", i))
            return dataBinary
    
    def set(self, newData):
        if (type(newData) != int):
            raise TypeError("Must provide data in int form!")
        else:
            self.dataList = [newData]
    
    def append(self, newData):
        if (type(newData) != int):
            raise TypeError("Must provide data in int form!")
        else:
            self.dataList.append(newData)
    
    def get(self, index):
        return self.dataList[index]

class ChunkFloat(Chunk):
    def __init__(self, ckID):
        super().__init__(ckID)
        self.dataList = []
    
    def dataToBin(self):
        if len(self.dataList) == 0:
            raise ValueError("Float chunk must contain at least one value!")
        else:
            dataBinary = bytearray()
            for i in self.dataList:
                dataBinary.extend(struct.pack("<f",i))
            return dataBinary
    
    def set(self, newData):
        if (type(newData) != int and type(newData) != float):
            raise TypeError("Must provide data in int or float form!")
        else:
            self.dataList = [newData]
    
    def append(self, newData):
        if (type(newData) != int and type(newData) != float):
            raise TypeError("Must provide data in int or float form!")
        else:
            self.dataList.append(newData)
    
    def get(self, index):
        return self.dataList[index]

class ChunkDouble(Chunk):
    def __init__(self, ckID):
        super().__init__(ckID)
        self.dataList = []
    
    def dataToBin(self):
        if len(self.dataList) == 0:
            raise ValueError("Double chunk must contain at least one value!")
        else:
            dataBinary = bytearray()
            for i in self.dataList:
                dataBinary.extend(struct.pack("<d",i))
            return dataBinary
    
    def set(self, newData):
        if (type(newData) != int and type(newData) != float):
            raise TypeError("Must provide data in int or float form!")
        else:
            self.dataList = [newData]
    
    def append(self, newData):
        if (type(newData) != int and type(newData) != float):
            raise TypeError("Must provide data in int or float form!")
        else:
            self.dataList.append(newData)
    
    def get(self, index):
        return self.dataList[index]

class Riff(Chunk):
    def __init__(self, formType):
        super().__init__("RIFF")
        self.formType = _checkFourChar(formType)
        self.dataList = []
    
    def getBinary(self):
        dataBinary = bytearray(self.formType.encode())
        dataBinary.extend(self.dataToBin())
        finalBinary = bytearray()
        finalBinary.extend(self.id.encode())
        finalBinary.extend(len(dataBinary).to_bytes(4, 'little'))
        finalBinary.extend(dataBinary)
        return finalBinary
    
    def dataToBin(self):
        if len(self.dataList) == 0:
            raise ValueError("Riff chunk must contain at least one subchunk!")
        else:
            dataBinary = bytearray()
            for i in self.dataList:
                dataBinary.extend(i.getBinary())
            return dataBinary
    
    def addChunk(self, chunk):
        if not isinstance(chunk, Chunk):
            raise TypeError("Must provide a Chunk or one of its subclasses!")
        else:
            self.dataList.append(chunk)

def _checkFourChar(fourChar):
    if type(fourChar) != str:
        raise TypeError("RIFF type must be a string!")
    elif len(fourChar) == 0:
        raise ValueError("Must specify a RIFF type!")
    elif fourChar[0] == " ":
        raise ValueError("RIFF type cannot start with whitespace!")
    elif len(fourChar) >= 4:
        return fourChar[0:4]
    else:
        while len(fourChar) < 4:
            fourChar += " "
        return fourChar

def runTest():
    testRiff = Riff("TEST")

    testChunk = Chunk("chnk")

    testBinChunk = ChunkBin("bin ")
    testBinChunk.set(bytearray("this is a test of setting arbitrary binary chunks".encode()))
    testBinChunk.extend(bytearray(" and appending more arbitrary data to them".encode()))

    testStrChunk = ChunkStr("str ")
    testStrChunk.set("this is a test of string chunks")
    testStrChunk.extend(" and this is a test of extending the string chunks")

    testInt32Chunk = ChunkInt32("i32 ")
    testInt32Chunk.set(12345678)
    testInt32Chunk.append(1431655765)
    testInt32Chunk.append(-1)
    testInt32Chunk.append(0)

    testInt16Chunk = ChunkInt16("i16 ")
    testInt16Chunk.set(12345)
    testInt16Chunk.append(21845)
    testInt16Chunk.append(-1)
    testInt16Chunk.append(0)

    testDoubleChunk = ChunkDouble("d64 ")
    testDoubleChunk.set(12345678.7654321)
    testDoubleChunk.append(0.000000000000001)
    testDoubleChunk.append(-1)
    testDoubleChunk.append(0)

    testFloatChunk = ChunkFloat("f32 ")
    testFloatChunk.set(123.4567)
    testFloatChunk.append(0.000001)
    testFloatChunk.append(-1)
    testFloatChunk.append(0)

    testRiff.addChunk(testChunk)
    testRiff.addChunk(testBinChunk)
    testRiff.addChunk(testStrChunk)
    testRiff.addChunk(testInt32Chunk)
    testRiff.addChunk(testInt16Chunk)
    testRiff.addChunk(testDoubleChunk)
    testRiff.addChunk(testFloatChunk)

    with open("testRIFF.riff", "wb") as f:
        f.write(bytes(testRiff.getBinary()))

if __name__ == "__main__":
    runTest()
