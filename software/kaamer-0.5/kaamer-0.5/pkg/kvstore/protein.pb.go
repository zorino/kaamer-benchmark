// Code generated by protoc-gen-go. DO NOT EDIT.
// source: protein.proto

package kvstore

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Protein struct {
	EntryId              string            `protobuf:"bytes,1,opt,name=EntryId,proto3" json:"EntryId,omitempty"`
	Sequence             string            `protobuf:"bytes,2,opt,name=Sequence,proto3" json:"Sequence,omitempty"`
	Length               int32             `protobuf:"varint,3,opt,name=Length,proto3" json:"Length,omitempty"`
	Features             map[string]string `protobuf:"bytes,4,rep,name=Features,proto3" json:"Features,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *Protein) Reset()         { *m = Protein{} }
func (m *Protein) String() string { return proto.CompactTextString(m) }
func (*Protein) ProtoMessage()    {}
func (*Protein) Descriptor() ([]byte, []int) {
	return fileDescriptor_b3c3736181c33c07, []int{0}
}

func (m *Protein) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Protein.Unmarshal(m, b)
}
func (m *Protein) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Protein.Marshal(b, m, deterministic)
}
func (m *Protein) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Protein.Merge(m, src)
}
func (m *Protein) XXX_Size() int {
	return xxx_messageInfo_Protein.Size(m)
}
func (m *Protein) XXX_DiscardUnknown() {
	xxx_messageInfo_Protein.DiscardUnknown(m)
}

var xxx_messageInfo_Protein proto.InternalMessageInfo

func (m *Protein) GetEntryId() string {
	if m != nil {
		return m.EntryId
	}
	return ""
}

func (m *Protein) GetSequence() string {
	if m != nil {
		return m.Sequence
	}
	return ""
}

func (m *Protein) GetLength() int32 {
	if m != nil {
		return m.Length
	}
	return 0
}

func (m *Protein) GetFeatures() map[string]string {
	if m != nil {
		return m.Features
	}
	return nil
}

func init() {
	proto.RegisterType((*Protein)(nil), "kvstore.Protein")
	proto.RegisterMapType((map[string]string)(nil), "kvstore.Protein.FeaturesEntry")
}

func init() { proto.RegisterFile("protein.proto", fileDescriptor_b3c3736181c33c07) }

var fileDescriptor_b3c3736181c33c07 = []byte{
	// 182 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x2d, 0x28, 0xca, 0x2f,
	0x49, 0xcd, 0xcc, 0xd3, 0x03, 0xd1, 0xf9, 0x42, 0xec, 0xd9, 0x65, 0xc5, 0x25, 0xf9, 0x45, 0xa9,
	0x4a, 0x17, 0x18, 0xb9, 0xd8, 0x03, 0x20, 0x52, 0x42, 0x12, 0x5c, 0xec, 0xae, 0x79, 0x25, 0x45,
	0x95, 0x9e, 0x29, 0x12, 0x8c, 0x0a, 0x8c, 0x1a, 0x9c, 0x41, 0x30, 0xae, 0x90, 0x14, 0x17, 0x47,
	0x70, 0x6a, 0x61, 0x69, 0x6a, 0x5e, 0x72, 0xaa, 0x04, 0x13, 0x58, 0x0a, 0xce, 0x17, 0x12, 0xe3,
	0x62, 0xf3, 0x49, 0xcd, 0x4b, 0x2f, 0xc9, 0x90, 0x60, 0x56, 0x60, 0xd4, 0x60, 0x0d, 0x82, 0xf2,
	0x84, 0xac, 0xb8, 0x38, 0xdc, 0x52, 0x13, 0x4b, 0x4a, 0x8b, 0x52, 0x8b, 0x25, 0x58, 0x14, 0x98,
	0x35, 0xb8, 0x8d, 0xe4, 0xf4, 0xa0, 0xb6, 0xea, 0x41, 0x6d, 0xd4, 0x83, 0x29, 0x00, 0xdb, 0x13,
	0x04, 0x57, 0x2f, 0x65, 0xcd, 0xc5, 0x8b, 0x22, 0x25, 0x24, 0xc0, 0xc5, 0x9c, 0x9d, 0x5a, 0x09,
	0x75, 0x16, 0x88, 0x29, 0x24, 0xc2, 0xc5, 0x5a, 0x96, 0x98, 0x53, 0x0a, 0x73, 0x0f, 0x84, 0x63,
	0xc5, 0x64, 0xc1, 0x98, 0xc4, 0x06, 0xf6, 0xa2, 0x31, 0x20, 0x00, 0x00, 0xff, 0xff, 0x4f, 0xf9,
	0x99, 0xd6, 0xf3, 0x00, 0x00, 0x00,
}
